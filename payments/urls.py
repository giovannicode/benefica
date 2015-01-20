from django.conf.urls import url, patterns

from payments import views

urlpatterns = patterns('',
    url('^$', views.PaymentView.as_view(), name='index'),
)
