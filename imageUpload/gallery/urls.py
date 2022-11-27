from django.urls import path ,include
from .views import PhotoListView, PhotoDetailView, PhotoDeleteView, UploadView

app_name = 'gallery'
urlpatterns = [
    path('', PhotoListView.as_view(), name = 'list'),
    path('gallery/<int:pk>/', PhotoDetailView.as_view(), name = 'detail'),
    path('gallery/upload/', UploadView.as_view(), name = 'upload'),
    path('gallery/<int:pk>/delete/', PhotoDeleteView.as_view(), name ='delete' ), 
]