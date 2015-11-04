
#from django.shortcuts import render  # boilerplate Django created code...

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

    
 # -*- coding: utf-8 -*-
# from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.conf import settings
import os


from .models import Document, User, Audio
from .forms import DocumentForm

# DELETE??
# import scipy.io.wavfile
# from scipy.io.wavfile import write



import numpy as np
import room_simulate
import subtract_audio

from django_rq import job 



def download(request):

    

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = User()       # create new user
            current_user.save()
    #           print current_user.id
            newdoc = Audio(user = current_user, file = request.FILES['docfile'])
            newdoc2 = Audio(user = current_user, file = request.FILES['docfile2'])

            newdoc.save()
            newdoc2.save()

            output_filename = os.path.splitext(os.path.basename(newdoc.file.url))[0]
            output_path = os.path.join(settings.MEDIA_ROOT,output_filename+'_SUBTRACTED.wav')
            print output_path


            # subtract_audio.subtract(newdoc, newdoc2)
            # subtract_audio.subtract.delay(newdoc, newdoc2)
            subtract_audio.subtract.delay(newdoc, newdoc2, current_user)
                
            documents = Audio.objects.all()
            # context = {'documents': documents, 'form': form, 'output_path': output_path}
            # return HttpResponseRedirect(reverse('index'))
        return HttpResponseRedirect(reverse('download'))
    else:
        form = DocumentForm() # A empty, unbound form
       

        
        # Load documents for the list page
    #     documents = Document.objects.all()
    documents = Audio.objects.all()
    
        # output_url = os.path.join(settings.MEDIA_ROOT, raw_audio_filename)  
    output_path = '/media/Ghosts_echoed_RIR_noise_testfile_SUBTRACTED.wav'
    context = {'documents': documents, 'form': form, 'output_path': output_path}
    #     context = {'documents': documents}

        # Render list page with the documents and the form
        # return render(request,'index.html', context)

    return render(request,'download.html', context)  
        

def index(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = User()       # create new user
            current_user.save()
#           print current_user.id
            newdoc = Audio(user = current_user, file = request.FILES['docfile'])
            newdoc2 = Audio(user = current_user, file = request.FILES['docfile2'])

            newdoc.save()
            newdoc2.save()

            
            # subtract_audio.subtract(newdoc, newdoc2)
            # subtract_audio.subtract.delay(newdoc, newdoc2)
            subtract_audio.subtract.delay(newdoc, newdoc2, current_user)
            
            # print newdoc.
            # newdoc_wav_path = newdoc.file 
            # print newdoc_wav_path
            # recording_path = os.path.join(settings.MEDIA_ROOT, 'newdoc.file' )

            # recording_path = os.path.join(settings.MEDIA_ROOT, 'GhostsNStuff_mono_4s.wav' )
            
            # rate, data = scipy.io.wavfile.read(recording_path)
            # u = data.astype(np.float64)
            # d = room_simulate.room_sim(u)
            # scaled_d = np.int16(d/np.max(np.abs(d)) * 32767)
            
            # output_path = os.path.join(settings.MEDIA_ROOT, 'GhostsNStuff_mono_4s_TEST.wav' )
            # write(output_path , 44100, scaled_d)
            
            # Redirect to the document list after POST
        # return HttpResponseRedirect(reverse('index'))
        return HttpResponseRedirect(reverse('download'))
    else:
        form = DocumentForm() # A empty, unbound form

    
    # Load documents for the list page
#     documents = Document.objects.all()
    documents = Audio.objects.all()
    context = {'documents': documents, 'form': form}
#     context = {'documents': documents}

    # Render list page with the documents and the form
    return render(request,'index.html', context)


# def list(request):
#     # Handle file upload
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#         	current_user = User()		# create new user
#         	current_user.save()
# #         	print current_user.id
#         	newdoc = Audio(user = current_user, file = request.FILES['docfile'])
#         	newdoc2 = Audio(user = current_user, file = request.FILES['docfile2'])

#         	newdoc.save()
#         	newdoc2.save()
        	
#         	recording_path = os.path.join(settings.MEDIA_ROOT, 'GhostsNStuff_mono_4s.wav' )
        	
#         	rate, data = scipy.io.wavfile.read(recording_path)
#         	u = data.astype(np.float64)
#         	d = room_simulate.room_sim(u)
#         	scaled_d = np.int16(d/np.max(np.abs(d)) * 32767)
        	
#         	output_path = os.path.join(settings.MEDIA_ROOT, 'GhostsNStuff_mono_4s_TEST.wav' )
#         	write(output_path , 44100, scaled_d)
			
#             # Redirect to the document list after POST
#         return HttpResponseRedirect(reverse('index'))
#     else:
#         form = DocumentForm() # A empty, unbound form

    
#     # Load documents for the list page
# #     documents = Document.objects.all()
#     documents = Audio.objects.all()
#     context = {'documents': documents, 'form': form}
# #     context = {'documents': documents}

#     # Render list page with the documents and the form
#     # return render(request,'audio_process/list.html', context)
#     return render(request,'index.html', context)
        
        
        