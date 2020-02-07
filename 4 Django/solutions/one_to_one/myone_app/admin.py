from django.contrib import admin

from .models import Key, Value

for _ in [Key, Value]:
    admin.site.register(_)

# Register your models here.
