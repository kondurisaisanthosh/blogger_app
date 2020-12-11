from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from PIL import Image
from django.db import models
from django.contrib.auth.models import User

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

    def save(self,*args, **kwargs):
        im = Image.open(self.image)
        if im.mode !='RGB':
            im = im.convert("RGB")
        output = BytesIO()
        im = im.resize((300, 300))
        im.save(output, format='JPEG', quality=100)
        output.seek(0)
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                          sys.getsizeof(output), None)
        super(Profile, self).save()