from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserForm, ProfileForm
from .models import Profile

admin.site.register(Profile)

# Register your models here.
