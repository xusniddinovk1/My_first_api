from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    objects = None
    title = models.CharField(max_length=255, null=False, blank=False)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
