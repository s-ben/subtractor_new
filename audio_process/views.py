
#from django.shortcuts import render  # boilerplate Django created code...

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, render_to_response

    
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

    # if request.session.test_cookie_worked():
    #     print ">>>> TEST COOKIE WORKED!"
    #     request.session.delete_test_cookie()

    print request.COOKIES

    if request.COOKIES.has_key('test_cookie'):
        print "test cookie value"
        print request.COOKIES['test_cookie']

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

            # Get filename of raw audio file (mixed audio)
            # output_path = 'https://s3-us-west-2.amazonaws.com/audiofiles1234/'+output_filename
            output_filename = os.path.splitext(os.path.basename(newdoc.file.url))[0]
            output_path = 'https://s3-us-west-2.amazonaws.com/audiofiles1234/'+output_filename
            # subtract_audio.subtract(newdoc, newdoc2)
            # subtract_audio.subtract.delay(newdoc, newdoc2)
            subtract_audio.subtract.delay(newdoc, newdoc2, current_user)
                
            documents = Audio.objects.all()
            # context = {'documents': documents, 'form': form, 'output_path': output_path}
            # return HttpResponseRedirect(reverse('index'))
        return HttpResponseRedirect(reverse('download'))
    else:
        form = DocumentForm() # A empty, unbound form
        output_path = 'https://s3-us-west-2.amazonaws.com/audiofiles1234/boogabooga'
       

        
        # Load documents for the list page
    #     documents = Document.objects.all()
    documents = Audio.objects.all()
    
    # output_filename = os.path.splitext(os.path.basename(newdoc.file.url))[0]
    # output_filename_s3 = output_filename+'_SUBTRACTED_TEST.wav'
    # output_path = 'https://s3-us-west-2.amazonaws.com/audiofiles1234/'+output_filename
    # # output_path = os.path.join(settings.MEDIA_ROOT,output_filename+'_SUBTRACTED.wav')
    # output_path = 'https://s3-us-west-2.amazonaws.com/audiofiles1234/'+output_filename_s3
        # output_url = os.path.join(settings.MEDIA_ROOT, raw_audio_filename)  
    # output_path = '/media/Ghosts_echoed_RIR_noise_testfile_SUBTRACTED.wav'
    # context = {'documents': documents, 'form': form, 'output_path': output_path}
    context = {'documents': documents, 'form': form, 'output_path': output_path}
    #     context = {'documents': documents}

        # Render list page with the documents and the form
        # return render(request,'index.html', context)

    return render(request,'download.html', context)  
        

def index(request):

    # response = HttpResponse()
    # response = render_to_response('rango/index.html', context_dict, context)

    # # request.session.set_test_cookie()
    # response = render_to_response('download.html')
    # response.set_cookie('test_cookie')

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
            context = {'form': form}
            # response = render_to_response('download.html', context, RequestContext(request))
            # response.set_cookie('test_cookie', 'test_value')

            
            # output_path = os.path.join(settings.MEDIA_ROOT, 'GhostsNStuff_mono_4s_TEST.wav' )
            # write(output_path , 44100, scaled_d)
            
            # Redirect to the document list after POST
        # return HttpResponseRedirect(reverse('index'))
        # return HttpResponseRedirect(reverse('download'))
            response = HttpResponseRedirect(reverse('download'))
            response.set_cookie('test_cookie', 'test_value')
        # return render(response,'download.html')
            return response
    else:
        form = DocumentForm() # A empty, unbound form

    
    # Load documents for the list page
#     documents = Document.objects.all()
    documents = Audio.objects.all()
    context = {'documents': documents, 'form': form}
#     context = {'documents': documents}

    # Render list page with the documents and the form
    return render(request,'index.html', context)


        
        
        