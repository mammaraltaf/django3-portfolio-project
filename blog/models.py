from django.db import models

# Create your models here.


class Blogs(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.title
