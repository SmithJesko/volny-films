from django.urls import path

from .views import index, media

urlpatterns = [
    path('', index, name='index'),
    path('media/<str:movie_id>', media, name='media'),
]