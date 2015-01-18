from django.conf.urls import url, patterns
from products import views

urlpatterns = patterns('',
    url(r'^add', views.ProductCreateView.as_view(), name='add'),
    url(r'^list', views.ProductListView.as_view(), name='list')
) 
