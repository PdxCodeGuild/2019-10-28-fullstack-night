from django.contrib import admin
from .models import Meal, DiaryDay, DiaryEntry, UserProfile

admin.site.register(Meal)
admin.site.register(DiaryDay)
admin.site.register(DiaryEntry)
admin.site.register(UserProfile)