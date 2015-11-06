"""subtractor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	
	
    url(r'^audio_process/', include('audio_process.urls')),
    url(r'^$', include('audio_process.urls')), # DELETE ONE PATH FOR AUDIO PROCESS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^django-rq/', include('django_rq.urls')) #PUT IN AUDIO_PROCESS AS WELL?
] 
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

# 
# from django.conf.urls import include, url
# from django.conf import settings
# from django.conf.urls.static import static
# from django.views.generic import RedirectView
# 
# from django.contrib import admin
# 
# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^audio_process/',include('subtractor.audio_process.urls')),
# #     url(r'^audio_process/',include('audio_process.urls')),
#     url(r'^$', RedirectView.as_view(url='/audio_process/list/', permanent=True)),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

