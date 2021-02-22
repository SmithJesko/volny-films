from collections import Counter
from datetime import datetime, timedelta

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from home.models import Movie
from .models import ClientConnection, UserClientConnection, MovieView


@login_required(login_url='/')
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
    movie_views_count = []
    movie_ranks = []
    for i in MovieView.objects.filter(media_type='movie'):
        if not i.movie_id in movie_views:
            movie_views.append(i.movie_id)
        movie_views_count.append(i.movie_id)
    for i in movie_views:
        views = sum(1 for a in movie_views_count if a == i)
        title = Movie.objects.filter(movie_id=i)[0].title
        movie_ranks.append((title, views))
    movie_ranks_sorted = sorted(movie_ranks, key=lambda x: (-x[1], x[0]))[:5]


    show_views = []
    show_views_count = []
    show_ranks = []
    for i in MovieView.objects.filter(media_type='series'):
        if not i.movie_id in show_views:
            show_views.append(i.movie_id)
        show_views_count.append(i.movie_id)
    for i in show_views:
        views = sum(1 for a in show_views_count if a == i)
        title = Movie.objects.filter(movie_id=i)[0].title
        show_ranks.append((title, views))
    show_ranks_sorted = sorted(show_ranks, key=lambda x: (-x[1], x[0]))[:5]

    all_connections = []
    for i in ClientConnection.objects.all().order_by('-timestamp'):
        all_connections.append(i)
    for i in UserClientConnection.objects.all().order_by('-timestamp'):
        all_connections.append(i)
    requests = all_connections[:25]

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
        'movie_ranks_sorted': movie_ranks_sorted,
        'show_ranks_sorted': show_ranks_sorted,
        'requests': requests,
    }
    return render(request, 'analytics/index.html', context)
