from django.contrib import admin

from .models import DiaryDay, DiaryEntry, Meal

admin.site.register(DiaryDay)
admin.site.register(DiaryEntry)
admin.site.register(Meal)