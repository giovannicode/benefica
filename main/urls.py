from django.conf.urls import patterns, url
from main import views
from products import views as products_views

urlpatterns = patterns('',
    url(r'^$', products_views.ProductListView.as_view(), name='index'),
    url(r'^$', views.index, name='index'),
)
