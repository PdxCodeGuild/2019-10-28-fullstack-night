from django import forms
from .models import Profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'location', 'bio', 'mediums', 'misc', 'favorites', 'theme', 'layout', 'instagram', 'patreon', 'soundcloud', 'profile_pic',)