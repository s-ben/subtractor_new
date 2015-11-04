import numpy as np
import os
from django.conf import settings

# from django.http import HttpResponse
# from django.shortcuts import render

    
 # -*- coding: utf-8 -*-
# from django.shortcuts import render_to_response
# from django.template import RequestContext
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse

from django.conf import settings
import os


from .models import Document, User, Audio
# from .forms import DocumentForm


# import scipy.io.wavfile
# from scipy.io.wavfile import write
import wave
import struct

import numpy as np
import adaptfilt as adf
import room_simulate


from django_rq import job
from django.core.files import File

@job
def subtract(newdoc, newdoc2, current_user):


    # newdoc_wav_path = newdoc.file 
    # print newdoc_wav_path


    # recording_path = os.path.join(settings.MEDIA_ROOT, newdoc.file )
    # print newdoc.file
    # type newdoc.file
    # print newdoc.file.url 

    # get paths for raw audio and music to be subtracted
    raw_audio_filename = os.path.basename(newdoc.file.url)
    original_audio_filename = os.path.basename(newdoc2.file.url)

    # newdoc_url = newdoc.file.url 
    # print type(newdoc_url)

    # Create paths to read in audio files
    recording_path = os.path.join(settings.MEDIA_ROOT, raw_audio_filename)
    original_audio_path = os.path.join(settings.MEDIA_ROOT, original_audio_filename)
    # recording_path = os.path.join(settings.BASE_DIR, newdoc_url)
    # print recording_path
    # print settings.BASE_DIR


    input_wav = wave.open (recording_path, "r")
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = input_wav.getparams ()
    frames = input_wav.readframes (nframes * nchannels)
    out = struct.unpack_from ("%dh" % nframes * nchannels, frames)

    r = np.asarray(out, np.float64)

    # rate, data = scipy.io.wavfile.read(recording_path)
    # r = data.astype(np.float64)

    input_wav = wave.open (original_audio_path, "r")
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = input_wav.getparams ()
    frames = input_wav.readframes (nframes * nchannels)
    out = struct.unpack_from ("%dh" % nframes * nchannels, frames)

    o = np.asarray(out, np.float64)

    # rate, data = scipy.io.wavfile.read(original_audio_path)
    # o = data.astype(np.float64)

    print len(o)
    print len(r)
    print 'applying adaptive filt'
    # Apply adaptive filter
    M = 100 #8000 (takelly long time) #100  # Number of filter taps in adaptive filter
    step = 0.1  # Step size
    y, e, w = adf.nlms(o, r, M, step, returnCoeffs=True)

    scaled_e = np.int16(e/np.max(np.abs(e)) * 32767)

    # d = room_simulate.room_sim(u)
    # scaled_d = np.int16(d/np.max(np.abs(d)) * 32767)
    
    # output_path = os.path.join(settings.MEDIA_ROOT, newdoc_filename+'TEST2.wav' )

    output_filename = os.path.splitext(os.path.basename(newdoc.file.url))[0]
    print output_filename

    output_path = os.path.join(settings.MEDIA_ROOT,output_filename+'_SUBTRACTED.wav')
    # output_path = os.path.join(settings.MEDIA_ROOT, ['/Ghosts_TEST2.wav'] )

    
    output_wav = wave.open (output_path, "w")
    output_wav.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
    output_wav.writeframes(scaled_e)

    # write(output_path , 44100, scaled_e)

    f = open(output_path)
    output_file = File(f)

    newdoc3 = Audio(user = current_user, file = output_file)
    newdoc3.save()
	
    return output_path
