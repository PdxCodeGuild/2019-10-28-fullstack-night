from django.contrib import admin
from .models import *

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(CheckoutStatus)


# Register your models here.
