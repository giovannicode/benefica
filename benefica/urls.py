from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'benefica.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^products/', include('products.urls', namespace='products')),
    url(r'^profiles/', include('profiles.urls', namespace='profiles')),
    url(r'^payments/', include('payments.urls', namespace='payments')),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^$', include('main.urls', namespace='main')),
    url(r'^admin/', include(admin.site.urls)),
)
