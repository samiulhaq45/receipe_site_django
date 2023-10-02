from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Receipe(models.Model):
    # adding user model to receipe as a foreign key.
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    # Model Schema for Receipe.
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to="images")
    