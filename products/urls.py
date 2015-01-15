from django.conf.urls import url, patterns
from products import views

urlpatterns = patterns('',
    url(r'^add/', views.add, name='add'),
) 
