from django.contrib import admin

from .models import ArtPiece, ArtCollection, CollectionPiece

admin.site.register(ArtPiece)
admin.site.register(ArtCollection)
admin.site.register(CollectionPiece)

# Register your models here.
