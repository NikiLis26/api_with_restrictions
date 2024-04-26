# from django.db import models
# from django.contrib.auth.models import User
#
#
# class Advertisement(models.Model):
#    STATUS_CHOICES = (
#        ('OPEN', 'Open'),
#        ('CLOSED', 'Closed'),
#    )
#
#    title = models.CharField(max_length=100)
#    description = models.TextField()
#    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
#    created_at = models.DateTimeField(auto_now_add=True)
#    author = models.ForeignKey(User, on_delete=models.CASCADE)

from django.db import models
from django.conf import settings

class Advertisement(models.Model):
   STATUS_CHOICES = (
       ('OPEN', 'Open'),
       ('CLOSED', 'Closed'),
   )

   title = models.CharField(max_length=100)
   description = models.TextField()
   status = models.CharField(max_length=10, choices=STATUS_CHOICES)
   created_at = models.DateTimeField(auto_now_add=True)
   author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
