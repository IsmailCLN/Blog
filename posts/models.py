from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_time = models.DateField('date published')

    def __str__(self):
        return self.title