from django.contrib.postgres.fields import JSONField
from django.db import models

from ..core.models import User


class LastRequestReposGithubApi(models.Model):
    available = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    githubApiUrls = JSONField(default='[]')
    lastTenReposSent = JSONField(default='[]')
    lastRequest = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    available.boolean = True

    def __str__(self):
        return self.user.username
