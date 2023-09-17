  

from django.db import models

#Creating model here

class Blog(models.Model):
    name = models.CharField(max_length=300)
    image = models.URLField()
    summary = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
    