from django.db import models

# Create your models here.


class project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio_code/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
