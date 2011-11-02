from models  import Note
from tagging.models import *
from django.shortcuts import render_to_response, redirect, HttpResponse
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required
def list_notes(request):
    notes = Note.objects.filter(owner=request.user)

    tags = Tag.objects.all() # ToDo change this into the users's most used tags
    c = {
        "note_list": notes,
        "tag_list": tags,
        "curr_user": request.user,
    }
    return render_to_response("mobilenotes/notes_list.html", c, context_instance=RequestContext(request))
    
@login_required
def list_notes_by_tag(request,tag):
    notes =  TaggedItem.objects.get_by_model(Note,'idea').filter(owner=request.user)
    c = {
        "note_list": notes,
        "curr_user": request.user,
    }
    return render_to_response("mobilenotes/notes_list.html", c, context_instance=RequestContext(request))

def view_note(request, note_id):
    print note_id
    note = Note.objects.filter(owner=request.user, id=note_id)[0]
    print note
    c = {
        "note": note,
        "curr_user": request.user,
    }
    print request.user
    return render_to_response("mobilenotes/note_view.html", c, context_instance=RequestContext(request))
    

