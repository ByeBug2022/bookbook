from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'helloworld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hello/', include('hello.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
