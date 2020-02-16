from django.contrib import admin
from .models import *

for thing in [Movie, Condition, Tape, Genre]:
    admin.site.register(thing)

# Register your models here.
