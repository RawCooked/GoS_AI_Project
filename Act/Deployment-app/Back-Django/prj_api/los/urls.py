
from django.urls import path
from . import views

urlpatterns = [
    path('classify_lab_event/', views.classify_lab_event, name='classify_lab_event'),
]