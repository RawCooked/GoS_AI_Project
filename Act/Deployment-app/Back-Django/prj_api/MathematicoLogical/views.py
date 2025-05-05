import requests
from django.shortcuts import render

def chat_view(request):
    response_text = ''
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        ollama_url = 'http://localhost:11500/api/generate'
        model_name = 'mistral:7b'  # or 'mistral:7b' if tagged

        response = requests.post(ollama_url, json={
            "model": model_name,
            "prompt": user_input,
            "stream": False
        })

        if response.ok:
            response_text = response.json().get('response', 'No response text found.')
        else:
            response_text = f"Error: {response.status_code} {response.text}"

    return render(request, 'chat_interface.html', {
        'response_text': response_text
    })


from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import UploadedImage
from .serializers import ImageSerializer

@method_decorator(csrf_exempt, name='dispatch')
class ImageUploadView(APIView):
    parser_classes = (MultiPartParser,)
    
    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import generics
from django.http import FileResponse
import os

from rest_framework.permissions import AllowAny

class ImageListCreateView(generics.ListCreateAPIView):
    queryset = UploadedImage.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [AllowAny]  # Allow access without authentication
    
    # This will automatically handle both GET and POST requests

class ImageDownloadView(generics.RetrieveAPIView):
    queryset = UploadedImage.objects.all()
    
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        file_path = instance.image.path
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), as_attachment=True)
        return Response({"error": "File not found"}, status=404)