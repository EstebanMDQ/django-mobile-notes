from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from views import *

urlpatterns = patterns('',
    # notes by tag
    (r'^list/([a-z0-9_-])', list_notes_by_tag),
    # notes listing
    (r'^list', list_notes),

    # note view
    (r'^view/([a-z0-9_-])', view_note),
    
)
