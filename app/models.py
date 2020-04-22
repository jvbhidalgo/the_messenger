from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #oneToMany

class Post(models.Model):
    title = models.CharField(max_length=60)
    conteudo = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

