from django.contrib.auth.models import AbstractUser
from django.db import models


# To modify the roles, if required.
class Role(models.Model):
    ADMIN = 'admin'

    ROLE_CHOICES = (
        (ADMIN, 'admin'),
    )

    name = models.CharField(max_length=15, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name


# To modify in the future, if required.
class User(AbstractUser):
    # role = models.ManyToManyField(Role, blank=True, null=True)
    pass
