from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class ProfileUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    telegram = models.CharField(max_length=50, null=True, blank=True)
    educational_institution = models.CharField(max_length=300, null=True, blank=True)
    faculty = models.CharField(max_length=250, null=True, blank=True)
    speciality = models.CharField(max_length=250, null=True, blank=True)
    course = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.user)
