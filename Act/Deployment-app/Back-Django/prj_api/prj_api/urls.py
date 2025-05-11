from django.contrib import admin
from django.urls import path, include
from MathematicoLogical import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
#router.register(r'images', ImageViewSet, basename='image')

# Ajouter dans urls.py


urlpatterns = [
    path('admin/', admin.site.urls),
        path('api/drawing/maha/', views.predict_view, name='predict'),
        path('api/audio/khalil/', views.predict_audio_view, name='predict_audio'),
        path('api/drawing/achref/', views.predict_drawing, name='predict_drawing'),
        # path('api/math/idriss', views.generate_text_view, name='generate_text'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)