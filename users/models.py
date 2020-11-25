import math
from PIL import Image, ImageOps
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as storage
from django.db import models
from sorl.thumbnail import get_thumbnail
from django.contrib.auth.models import User
from storages.backends.s3boto3 import S3Boto3Storage
from django_resized import ResizedImageField

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile-pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs):
    #     super(Profile, self).save(*args, **kwargs)
    #     img=Image.open(self.image.path)
    #     if img.height>300 or img.width>300:
    #         output=(300,300)
    #         img.thumbnail(output)
    #         img.save(self.image.path)