from django.conf.urls import patterns, include, url

from django.contrib import admin
#from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sweepmate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #(r'^$', direct_to_template, {'template': 'index.html'})
    (r'^sweeps/$', 'sweep.views.SweepAll'),
    (r'^sweeps/(?P<sweepslug>.*)/', 'sweep.views.SweepDetail'),
)
