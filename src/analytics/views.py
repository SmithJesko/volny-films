from datetime import datetime, timedelta
from django.shortcuts import render

from home.models import Movie
from .models import ClientConnection, UserClientConnection, MovieView

def index(request):
    last_day = datetime.today() - timedelta(days=1)
    last_month = datetime.today() - timedelta(days=30)
    daily_visitors = ClientConnection.objects.filter(timestamp__gte=last_day).count() + UserClientConnection.objects.filter(timestamp__gte=last_day).count()
    monthly_visitors = ClientConnection.objects.filter(timestamp__gte=last_month).count() + UserClientConnection.objects.filter(timestamp__gte=last_month).count()
    total_visitors = ClientConnection.objects.all().count() + UserClientConnection.objects.all().count()

    total_movies = Movie.objects.filter(media_type="movie").count()
    total_shows = Movie.objects.filter(media_type="series").count()
    total_media = Movie.objects.all().count()

    movie_views = []
    for i in MovieView.objects.filter(media_type='movie'):
        if not i.movie_id in movie_views:
            movie_views.append(i.movie_id)

    show_views = []
    for i in MovieView.objects.filter(media_type='series'):
        if not i.movie_id in show_views:
            show_views.append(i.movie_id)

    context = {
        'daily_visitors': daily_visitors,
        'monthly_visitors': monthly_visitors,
        'total_visitors': total_visitors,
        'total_movies': total_movies,
        'total_shows': total_shows,
        'total_media': total_media,
        'shows_watched': len(show_views),
        'total_show_views': MovieView.objects.filter(media_type='series').count(),
        'movies_watched': len(movie_views),
        'total_movie_views': MovieView.objects.filter(media_type='movie').count(),
    }
    return render(request, 'analytics/index.html', context)
