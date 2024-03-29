from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mobile_notes_web.views.home', name='home'),
    # url(r'^mobile_notes_web/', include('mobile_notes_web.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


    # homepage
    url(r'^$', direct_to_template, {'template': 'homepage.html',}),
    
    # django registration
    (r'^accounts/', include('registration.urls')),

    # mobile notes
    (r'^notes/', include('mobilenotes.urls')),
    
)
