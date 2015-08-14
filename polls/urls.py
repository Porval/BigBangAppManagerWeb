from django.conf.urls import patterns, url

import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
     # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^apk/(?P<apk>.*)/$', views.apk_detail, name='apk_detial'),
]
