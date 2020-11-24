from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    print(image)
    print('saisantosh')

    # image = ResizedImageField(size=[300, 300],default='default.jpg', upload_to='profile_pics', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs):
    #     super(Profile, self).save(*args, **kwargs)
    #     img=Image.open(self.image.path)
    #     if img.height>300 or img.width>300:
    #         output=(300,300)
    #         img.thumbnail(output)
    #         img.save(self.image.path)


        #
        # class Posts(models.Model):
        #     title = models.CharField(max_length=200, blank=True)
        #     body = models.TextField(blank=True)
        #     created_at = models.DateTimeField(default=datetime.datetime.now)
        #     post_image = ResizedImageField(size=[500, 300], upload_to=get_image_path, blank=True, null=True)
        #
        #     def __str__(self):
        #         return self.title