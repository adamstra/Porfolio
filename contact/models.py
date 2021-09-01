from django.db import models

# Create your models here.


class contactModel(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.username
