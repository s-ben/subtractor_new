from django.conf.urls import url

from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^download$', views.download, name='download'),
    # url(r'^details/(?P<question_id>[0-9]+)$', views.details ),
    # url(r'^list/$', views.list, name='list'),
#     url(r'^lists/', views.list, name='index'),
] 
# if settings.DEBUG:
#     urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# name='detail'
# (?P<question_id>[0-9]+)/$

# -*- coding: utf-8 -*-
# from django.conf.urls import patterns, url
# 
# urlpatterns = patterns('subtractor.audio_process.views',
#     url(r'^list/$', 'list', name='list'),
# )