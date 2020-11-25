from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile
from sorl.thumbnail import get_thumbnail



class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
    #
    # def save(self):
    #     instance = super(ProfileUpdateForm, self).save(commit=False)
    #     # import ipdb;ipdb.set_trace()
    #     resized=get_thumbnail(instance.image, "300")
    #     instance.image.save(resized, True)
    #     instance.save()
    #     return instance