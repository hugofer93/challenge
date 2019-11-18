from django.contrib.postgres.fields import JSONField
from django.db import models

from ..core.models import User


# Create your models here.
class LastRepositoryApi(models.Model):
    available = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    repositories = JSONField()

    def __str__(self):
        return self.user


# Only save one User per request to Github Api
class LastQueryApi(models.Model):
    available = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    uri = models.URLField(max_length=100)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user
