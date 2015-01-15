from django.conf.urls import patterns, url
from account import views

urlpatterns = patterns('',
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^signout/$', views.signout, name='signout'),
)

