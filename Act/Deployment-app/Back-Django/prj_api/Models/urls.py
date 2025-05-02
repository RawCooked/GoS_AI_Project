from django.urls import path
from . import views

urlpatterns = [
    # Parent API
    path('parents/', views.ParentListCreate.as_view(), name='parent-list-create'),
    path('parents/<int:pk>/', views.ParentDetail.as_view(), name='parent-detail'),

    # Child API
    path('children/', views.ChildListCreate.as_view(), name='child-list-create'),
    path('children/<int:pk>/', views.ChildDetail.as_view(), name='child-detail'),
]
