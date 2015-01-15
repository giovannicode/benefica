from django.conf.urls import url, patterns
from profiles import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
