from django.db import models
import uuid


class TimeStampedModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True , db_index=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Extensions(TimeStampedModel):
    uuid = models.UUIDField(db_index=True , default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

        
