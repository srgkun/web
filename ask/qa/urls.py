from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', 'qa.views.test'),
    url(r'^signup/$', 'qa.views.test'),
    url(r'^ask/$', 'qa.views.test'),
    url(r'^ask//popular/$', 'qa.views.test'),
    url(r'^popular/$', views.popular, name='popular'),
    url(r'^new/$', 'qa.views.test'),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.one_question, name='one_question')
]
