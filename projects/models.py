from django.db import models


# Tehnology model
class Technology(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Project model
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology)
    progress = models.IntegerField()
    link = models.URLField(max_length=200, blank=True)
