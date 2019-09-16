from django.shortcuts import render

from django.shortcuts import render
from rest_framework import generics
from .models import Notes
from .serializers import NotesSerializer
from rest_framework import viewsets

class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer