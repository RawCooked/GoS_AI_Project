from django.contrib import admin
from django.urls import path, include
from MathematicoLogical import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from MathematicoLogical.views import  download_image
from rest_framework.routers import DefaultRouter
from django.urls import path
from MathematicoLogical.views import ImageUploadView,ImageListCreateView, ImageDownloadView


router = DefaultRouter()
#router.register(r'images', ImageViewSet, basename='image')


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.chat_view, name="chat_view"),
        path('/model', include('Models.urls')),  # Use actual app name here
            #path('api/images/<int:pk>/download/', download_image, name='download-image'),
    path('api/images/', ImageListCreateView.as_view(), name='image-list-create'),
        path('api/images/<int:pk>/download/', ImageDownloadView.as_view(), name='image-download'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)