from django.conf.urls import url, patterns

from carts import views

urlpatterns = patterns('',
    url(r'^$', views.CartView.as_view(), name='index'),
)
