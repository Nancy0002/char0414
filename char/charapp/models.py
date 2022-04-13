from django.db import models

# Create your models here.
class Char(models.Model):
    username=models.CharField(max_length=256)
    title=models.CharField(max_length=512)
    content=models.TextField(max_length=256)
    publish=models.DateTimeField()
    
    def __str__(self):
        return self.title

class Meta:
        ordering = ('-publish',)