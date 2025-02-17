from django.urls import path
from .views import media_list, upload_media, delete_media

urlpatterns = [
    path('', media_list, name='media_list'),
    path('upload/', upload_media, name='upload_media'),
    path('delete/<int:media_id>/', delete_media, name='delete_media'),  # Define delete_media route

]
