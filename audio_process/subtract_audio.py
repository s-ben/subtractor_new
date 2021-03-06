import numpy as np
import os
from django.conf import settings



from .models import Document, User, Audio
# from .forms import DocumentForm


# import scipy.io.wavfile
# from scipy.io.wavfile import write
import wave
import struct

import numpy as np
import adaptfilt as adf
import room_simulate  # DELETE?


from django_rq import job
from django.core.files import File
import urllib2
from boto.s3.connection import S3Connection
from boto.s3.key import Key

import StringIO

@job
def subtract(newdoc, newdoc2, current_user):


    # Connect to Amazon S3
    conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
    bucket = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME) 
    k = Key(bucket)


    # get filenames of raw audio and music to be subtracted
    raw_audio_filename = os.path.basename(newdoc.file.url)
    original_audio_filename = os.path.basename(newdoc2.file.url)

    # Create upload paths to S3 for mixed audio
    # raw_audio_s3_path = 'https://s3-us-west-2.amazonaws.com/audiofiles1234/'+raw_audio_filename
    # original_audio_s3_path = 'https://s3-us-west-2.amazonaws.com/audiofiles1234/'+original_audio_filename

    # Upload raw input to S3
    k.key = raw_audio_filename#testes#output_filename     # for now, key for bucket is filename (might want to change this in case of duplicates)
    k.set_contents_from_file(newdoc.file, rewind=True)
    k.make_public()

    # Upload original audio to S3
    k.key = original_audio_filename#testes#output_filename     # for now, key for bucket is filename (might want to change this in case of duplicates)
    k.set_contents_from_file(newdoc2.file, rewind=True)
    k.make_public()


    # Load file from AWS S3 
    url = "https://s3-us-west-2.amazonaws.com/audiofiles1234/Ghosts_echoed_RIR_noise_testfile.wav"
    recorded_audio_file = urllib2.urlopen(url)
    input_wav = wave.open (recorded_audio_file, "r")
    # input_wav = wave.open (newdoc.file, "r") #attempt (failed?) at opening file directly from filefield object

    # input_wav = wave.open (recording_path, "r")     # READING FROM DISK METHOD (PUT BACK IN?)

    # Read wav file into numpy array
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = input_wav.getparams ()
    frames = input_wav.readframes (nframes * nchannels)
    out = struct.unpack_from ("%dh" % nframes * nchannels, frames)

    r = np.asarray(out, np.float64)


    # Download file from AWS S3 
    url = "https://s3-us-west-2.amazonaws.com/audiofiles1234/GhostsNStuff_mono_4s.wav"
    original_audio_file = urllib2.urlopen(url)
    input_wav = wave.open (original_audio_file, "r")

    # input_wav = wave.open (original_audio_path, "r")    # READING FROM DISK METHOD (PUT BACK IN?)

    # Read wav file into numpy array
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = input_wav.getparams ()
    frames = input_wav.readframes (nframes * nchannels)
    out = struct.unpack_from ("%dh" % nframes * nchannels, frames)

    o = np.asarray(out, np.float64)


    # print len(o)
    # print len(r)
    # print 'applying adaptive filt'

    # Apply adaptive filter
    M = 100 #8000 (takelly long time) #100  # Number of filter taps in adaptive filter
    step = 0.1  # Step size
    y, e, w = adf.nlms(o, r, M, step, returnCoeffs=True)

    scaled_e = np.int16(e/np.max(np.abs(e)) * 32767)

    # Create output filename
    output_filename = os.path.splitext(os.path.basename(newdoc.file.url))[0]
    print output_filename
    output_filename_s3 = output_filename+'_SUBTRACTED_TEST.wav'

    # output_path = os.path.join(settings.MEDIA_ROOT,output_filename+'_SUBTRACTED.wav')
    output_path = 'https://s3-us-west-2.amazonaws.com/audiofiles1234/'+output_filename_s3


    # Write output wav to S3
    output_file = open(output_filename_s3, "w+")   # create pointer to file object

    output_wav = wave.open (output_file, "w")       
    output_wav.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
    output_wav.writeframes(scaled_e)

    # output_wav.seek(0)
    # output_filename_s3 = output_filename+'TEST'
    k.key = output_filename_s3#testes#output_filename     # for now, key for bucket is filename (might want to change this in case of duplicates)
    k.set_contents_from_file(output_file, rewind=True)
    k.make_public()


    # write(output_path , 44100, scaled_e)

    # f = open(output_path)
    # output_file = File(f)

    # newdoc3 = Audio(user = current_user, file = output_file)
    # newdoc3.save()
	
    return output_path
