from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework import viewsets
from .serializers import PlayerSerializer
from .models import Player
from .models import PlayerPhoto
from .serializers import PhotoSerializer
from rest_framework import generics

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().order_by('name')
    serializer_class = PlayerSerializer

    

# class PlayerPhotoViewSet(viewsets.ModelViewSet):
    
#     queryset = PlayerPhoto.objects.all()
#     serializer_class = PhotoSerializer


class PlayerPhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer

    def get_queryset(self):
        return PlayerPhoto.objects.filter(owner=self.request.user)

    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)




