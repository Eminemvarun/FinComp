from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    #updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    #timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
