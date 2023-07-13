from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    snippet = models.CharField(max_length=300)
    body = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.title