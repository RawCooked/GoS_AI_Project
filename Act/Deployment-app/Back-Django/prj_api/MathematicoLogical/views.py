import requests
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import UploadedImage
from .serializers import ImageSerializer
from rest_framework import generics
from django.http import FileResponse
import os
import numpy as np
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model as load_audio_model


import tensorflow as tf
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
import librosa

#!Idriss Api Call to Ollama wakahaou
MODEL_NAME= "qwen3:0.6b"



#!Travail Maha


# Charger le modèle MobileNetV2 sauvegardé
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models/model.h5')
model = load_model(MODEL_PATH)

# Pour preprocessing MobileNetV2
preprocess_input = tf.keras.applications.mobilenet_v2.preprocess_input
IMG_SIZE = (224, 224)  # Doit correspondre à ce qui a été utilisé à l'entraînement

# Fonction de prédiction
def predict_image(img_path):
    # Charger et prétraiter l'image
    img = image.load_img(img_path, target_size=IMG_SIZE)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Prédiction
    prediction = model.predict(img_array)[0][0]
    label = "talented" if prediction > 0.5 else "not talented"
    confidence = round(float(prediction) * 100, 2) if prediction > 0.5 else round(float(100 - prediction * 100), 2)

    return label, confidence


@csrf_exempt
def predict_view(request):
    if request.method == 'POST':
        # Vérifier la présence de l'image
        if 'image' not in request.FILES:
            return JsonResponse({'error': 'Aucune image fournie'}, status=400)

        try:
            # Sauvegarder l'image temporairement
            img_file = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(img_file.name, img_file)
            img_path = fs.path(filename)

            # Faire la prédiction
            label, confidence = predict_image(img_path)

            # Nettoyer le fichier temporaire
            fs.delete(filename)

            # Formater la réponse
            return JsonResponse({
                'result': label,
                'confidence': f"{confidence}%",
                'interpretation': 'Talented in drawing' if label == 'talented' else 'Needs improvement'
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)

    
#A7la delegué

# Add these imports at the top



# Audio model constants and loading (add this with your other model loading)
AUDIO_MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models/belle_voix_model.h5')
audio_model = load_audio_model(AUDIO_MODEL_PATH)

# Audio constants
SAMPLE_RATE = 22050
DURATION = 3
SAMPLES_PER_TRACK = SAMPLE_RATE * DURATION
FIXED_TIME_STEPS = 130

# Audio preprocessing function
def preprocess_audio(file_path):
    try:
        y, sr = librosa.load(file_path, sr=SAMPLE_RATE, duration=DURATION)
        
        if len(y) < SAMPLES_PER_TRACK:
            y = np.pad(y, (0, SAMPLES_PER_TRACK - len(y)))
        else:
            y = y[:SAMPLES_PER_TRACK]
            
        mel = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
        mel_db = librosa.power_to_db(mel, ref=np.max).astype(np.float32)
        
        if mel_db.shape[1] < FIXED_TIME_STEPS:
            mel_db = np.pad(mel_db, ((0, 0), (0, FIXED_TIME_STEPS - mel_db.shape[1])), mode='constant')
        else:
            mel_db = mel_db[:, :FIXED_TIME_STEPS]
            
        mel_db = (mel_db - mel_db.min()) / (mel_db.max() - mel_db.min() + 1e-8)
        return mel_db[np.newaxis, ..., np.newaxis]
    except Exception as e:
        raise ValueError(f"Audio preprocessing error: {str(e)}")

# Audio prediction view
@csrf_exempt
def predict_audio_view(request):
    if request.method == 'POST':
        # Check if audio file exists
        if 'audio' not in request.FILES:
            return JsonResponse({'error': 'No audio file provided'}, status=400)

        try:
            # Save the file temporarily
            audio_file = request.FILES['audio']
            fs = FileSystemStorage()
            filename = fs.save(audio_file.name, audio_file)
            audio_path = fs.path(filename)

            # Preprocess and predict
            features = preprocess_audio(audio_path)
            prediction = audio_model.predict(features)[0][0]
            label = "belle_voix" if prediction > 0.5 else "non_belle_voix"
            confidence = round(float(prediction) * 100, 2) if prediction > 0.5 else round(float(100 - prediction * 100), 2)

            # Clean up
            fs.delete(filename)

            # Format response
            return JsonResponse({
                'result': label,
                'confidence': f"{confidence}%",
                'interpretation': 'Beautiful voice' if label == 'belle_voix' else 'Needs vocal training'
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Method not allowed'}, status=405)

#Achref 


# Add these imports at the top with your other imports
import torch
from torchvision import models
from PIL import Image
# Add this function to safely load your model
def load_torch_model():
    try:
        # If using a standard ResNet
        with torch.serialization.safe_globals([models.resnet.ResNet]):
            model = torch.load(
                'MathematicoLogical/models/my_model.pt',
                map_location=torch.device('cpu'),
                weights_only=False
            )
        model.eval()
        print("PyTorch model loaded successfully!")
        return model
    except Exception as e:
        print(f"Failed to load PyTorch model: {str(e)}")
        return None

# Load the model when Django starts

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
import torch
from torchvision import transforms
from PIL import Image
import os
import numpy as np

# Define the transform globally
torch_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

torch_model = load_torch_model()
@csrf_exempt
def predict_drawing(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST method allowed'}, status=405)
    
    if not torch_model:
        return JsonResponse({'error': 'Model not loaded - server error'}, status=500)
    
    if 'image' not in request.FILES:
        return JsonResponse({'error': 'No image provided'}, status=400)

    fs = FileSystemStorage()
    try:
        # Save uploaded file temporarily
        uploaded_file = request.FILES['image']
        filename = fs.save(uploaded_file.name, uploaded_file)
        filepath = fs.path(filename)

        # Process image
        img = Image.open(filepath).convert("RGB")
        input_tensor = torch_transform(img).unsqueeze(0)

        # Make prediction
        with torch.no_grad():
            output = torch_model(input_tensor)
            probabilities = torch.nn.functional.softmax(output, dim=1)[0]
            prediction = torch.argmax(output, 1).item()
            confidence = round(float(probabilities[prediction]) * 100, 2)

        # Prepare response
        response = {
            'prediction': 'Talented' if prediction == 1 else 'Not Talented',
            'confidence': confidence,
            'interpretation': 'Showing artistic talent' if prediction == 1 else 'Needs more practice'
        }

        return JsonResponse(response)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
    finally:
        # Clean up file if it was created
        if 'filename' in locals():
            fs.delete(filename)