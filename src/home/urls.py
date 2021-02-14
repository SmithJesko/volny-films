from django.urls import path

from .views import index, media, search, report_a_bug

urlpatterns = [
    path('', index, name='index'),
    path('media/<str:movie_id>', media, name='media'),
    path('search/<str:qstr>', search, name='search'),
    path('report-a-bug/', report_a_bug, name='report-a-bug'),
]