from django.db import models
from fields import UUIDField
from tagging import 

class Notes(models.Model):
    id = UUIDField(primary_key=True, editable=False)
    title = models.CharField(max_lenght=50)
    content = models.TextField()
    tag = Tagging.Field()


