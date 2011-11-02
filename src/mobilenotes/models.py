from django.db import models
#from uuidfield import UUIDField
from tagging import register as tagging_register
from tagging.fields import TagField
from django.contrib.auth.models import User

class Note(models.Model):
#    uuid = UUIDField(primary_key=True, editable=False)
    title = models.CharField(max_length=50)
    content = models.TextField()
    tag = TagField()
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.title


tagging_register(Note)