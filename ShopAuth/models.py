from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):

    # This line of code is used to delete the profile page of a user when the account of that user is deleted.
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pictures', default="")
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username
