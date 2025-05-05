from django.contrib import admin
from django.urls import path, include
from MathematicoLogical import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.chat_view, name="chat_view"),
        path('/model', include('Models.urls')),  # Use actual app name here

]
