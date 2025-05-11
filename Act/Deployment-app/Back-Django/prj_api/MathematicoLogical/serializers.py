from rest_framework import serializers
from .models import UploadedImage

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ['id', 'title', 'image', 'uploaded_at']
        read_only_fields = ['uploaded_at']