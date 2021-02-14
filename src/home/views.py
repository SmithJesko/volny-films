from django.shortcuts import render

import json
import requests
from requests.exceptions import HTTPError
import urllib.request

from .models import Movie
from .secrets import tmdb_key, player_key


def index(request):
    qs = Movie.objects.all()
    urls = {
        'popular_movies': 'https://api.themoviedb.org/3/movie/popular?api_key=25b5fe2c16a3d43e789fb1b629b5db46&language=en-US&region=us',
        'top_rated_movies': 'https://api.themoviedb.org/3/movie/top_rated?api_key=25b5fe2c16a3d43e789fb1b629b5db46&language=en-US&region=us',
        'now_playing_movies': 'https://api.themoviedb.org/3/movie/now_playing?api_key=25b5fe2c16a3d43e789fb1b629b5db46&language=en-US&region=us',
        # 'popular_tv': 'https://api.themoviedb.org/3/tv/popular?api_key=25b5fe2c16a3d43e789fb1b629b5db46&language=en-US&page=1',
    }

    popular_movies_list = []
    top_rated_movies_list = []
    now_playing_movies_list = []
    popular_tv_list = []

    for key, value in urls.items():
        try:
            req = urllib.request.Request(url = value)
        except Exception as err:
            print(f'Error occurred: {err}')
        else:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                for i in data["results"]:
                    if not Movie.objects.filter(movie_id=i["id"]).exists():
                        new_movie = Movie(movie_id=i["id"], title=i["original_title"], overview=i["overview"], popularity=i["popularity"], poster=i["poster_path"], release_date=i["release_date"], language=i["original_language"], added=key)
                        new_movie.save()
                    if key == 'popular_movies':
                        popular_movies_list.append(i["id"])
                    elif key == 'top_rated_movies':
                        top_rated_movies_list.append(i["id"])
                    elif key == 'now_playing_movies':
                        now_playing_movies_list.append(i["id"])
                    elif key == 'popular_tv':
                        popular_tv_list.append(i["id"])

    popular_movies = Movie.objects.filter(movie_id__in=popular_movies_list)
    top_rated_movies = Movie.objects.filter(movie_id__in=top_rated_movies_list)
    now_playing_movies = Movie.objects.filter(movie_id__in=now_playing_movies_list)
    popular_tv = Movie.objects.filter(movie_id__in=popular_tv_list)
    context = {
        'popular_movies': popular_movies,
        'top_rated_movies': top_rated_movies,
        'now_playing_movies': now_playing_movies,
        'popular_tv_list': popular_tv_list,
        'data': data["results"]
    }
    # print(popular_movies)
    return render(request, 'index.html', context)

def media(request, movie_id):
    media = Movie.objects.get(movie_id=movie_id)

    context = {
        'media': media,
    }
    return render(request, 'media.html', context)


