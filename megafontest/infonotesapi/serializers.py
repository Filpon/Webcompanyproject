from .models import Notes
from rest_framework import serializers

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ("title", "slug", "description", "price")