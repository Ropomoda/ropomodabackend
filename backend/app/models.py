from django.db import models
import uuid
from safedelete.models import SafeDeleteModel , SOFT_DELETE_CASCADE

class TimeStampedModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True , db_index=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
class BaseUUIDModel(models.Model):
    uuid = models.UUIDField(db_index=True , default=uuid.uuid4, editable=False)
    class Meta:
        abstract = True
class Extensions(BaseUUIDModel,TimeStampedModel,SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        abstract = True

        
