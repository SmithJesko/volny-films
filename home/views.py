from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.urls import resolve

import json
import requests
from requests.exceptions import HTTPError
import urllib.request

from analytics.models import ClientConnection, UserClientConnection, MovieView
from analytics.utils import get_client_ip, IPInfo, page_view

from .models import Movie
from .forms import SearchForm
from .secrets import tmdb_key, omdb_key, player_key


def index(request):
    # Analytics
    page_view(request)
                
    # Search Form
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            return redirect('/search/{}'.format(form.cleaned_data['search']))
    else:
        form = SearchForm()

    qs = Movie.objects.all()
    urls = {
        'popular_movies': 'https://api.themoviedb.org/3/movie/popular?api_key={}&language=en-US&region=us'.format(tmdb_key),
        'top_rated_movies': 'https://api.themoviedb.org/3/movie/top_rated?api_key={}&language=en-US&region=us'.format(tmdb_key),
        'now_playing_movies': 'https://api.themoviedb.org/3/movie/now_playing?api_key={}&language=en-US&region=us'.format(tmdb_key),
        'popular_tv': 'https://api.themoviedb.org/3/tv/popular?api_key={}&language=en-US&page=1&region=us'.format(tmdb_key),
        'top_rated_tv': 'https://api.themoviedb.org/3/tv/top_rated?api_key={}&language=en-US&page=1&region=us'.format(tmdb_key),
        'on_the_air_tv': 'https://api.themoviedb.org/3/tv/on_the_air?api_key={}&language=en-US&page=1&region=us'.format(tmdb_key),
    }

    popular_movies_list = []
    top_rated_movies_list = []
    now_playing_movies_list = []
    popular_tv_list = []
    top_rated_tv_list = []
    on_the_air_tv_list = []

    for key, value in urls.items():
        try:
            req = urllib.request.Request(url = value)
        except Exception as err:
            print(f'Error occurred: {err}')
        else:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                for i in data["results"]:
                    try:
                        if Movie.objects.filter(movie_id=i["id"]).exists():
                            obj = Movie.objects.get(movie_id=i["id"])
                            obj.added = key
                            obj.save()
                        if not Movie.objects.filter(movie_id=i["id"]).exists():
                            if "original_title" in i:
                                with urllib.request.urlopen('https://api.themoviedb.org/3/movie/{}/external_ids?api_key={}'.format(i["id"], tmdb_key)) as resp:
                                    data = json.loads(resp.read().decode("utf-8"))
                                    imdb_id = data["imdb_id"]
                            elif "original_name" in i:
                                with urllib.request.urlopen('https://api.themoviedb.org/3/tv/{}/external_ids?api_key={}'.format(i["id"], tmdb_key)) as resp:
                                    data = json.loads(resp.read().decode("utf-8"))
                                    imdb_id = data["imdb_id"]
                            with urllib.request.urlopen('https://www.omdbapi.com?apikey={}&i={}&plot=full'.format(omdb_key, imdb_id)) as resp:
                                data = json.loads(resp.read().decode("utf-8"))
                                rated = data["Rated"]
                                runtime = data["Runtime"]
                                genre = data["Genre"]
                                director = data["Director"]
                                writer = data["Writer"]
                                actors = data["Actors"]
                                plot = data["Plot"]
                                awards = data["Awards"]
                                imdb_rating = data["imdbRating"]
                                media_type = data["Type"]
                            if "original_title" in i:
                                new_movie = Movie(movie_id=i["id"],
                                                imdb_id=imdb_id,
                                                title=i["original_title"],
                                                overview=i["overview"],
                                                popularity=i["popularity"],
                                                poster=i["poster_path"],
                                                release_date=i["release_date"],
                                                language=i["original_language"],
                                                added=key,
                                                rated = rated,
                                                runtime = runtime,
                                                genre = genre,
                                                director = director,
                                                writer = writer,
                                                actors = actors,
                                                plot = plot,
                                                awards = awards,
                                                imdb_rating = imdb_rating,
                                                media_type = media_type)
                                new_movie.save()
                            elif "original_name" in i:
                                new_movie = Movie(movie_id=i["id"],
                                                imdb_id=imdb_id,
                                                title=i["original_name"],
                                                overview=i["overview"],
                                                popularity=i["popularity"],
                                                poster=i["poster_path"],
                                                release_date=i["first_air_date"],
                                                language=i["original_language"],
                                                added=key,
                                                rated = rated,
                                                runtime = runtime,
                                                genre = genre,
                                                director = director,
                                                writer = writer,
                                                actors = actors,
                                                plot = plot,
                                                awards = awards,
                                                imdb_rating = imdb_rating,
                                                media_type = media_type)
                                new_movie.save()
                        if key == 'popular_movies':
                            popular_movies_list.append(i["id"])
                        elif key == 'top_rated_movies':
                            top_rated_movies_list.append(i["id"])
                        elif key == 'now_playing_movies':
                            now_playing_movies_list.append(i["id"])
                        elif key == 'popular_tv':
                            popular_tv_list.append(i["id"])
                        elif key == 'top_rated_tv':
                            top_rated_tv_list.append(i["id"])
                        elif key == 'on_the_air_tv':
                            on_the_air_tv_list.append(i["id"])
                    except Exception as err:
                        print(err)

    popular_movies = Movie.objects.filter(movie_id__in=popular_movies_list)
    top_rated_movies = Movie.objects.filter(movie_id__in=top_rated_movies_list)
    now_playing_movies = Movie.objects.filter(movie_id__in=now_playing_movies_list)
    popular_tv = Movie.objects.filter(movie_id__in=popular_tv_list)
    top_rated_tv = Movie.objects.filter(movie_id__in=top_rated_tv_list)
    on_the_air_tv = Movie.objects.filter(movie_id__in=on_the_air_tv_list)

    context = {
        'popular_movies': popular_movies,
        'top_rated_movies': top_rated_movies,
        'now_playing_movies': now_playing_movies,
        'popular_tv': popular_tv,
        'top_rated_tv': top_rated_tv,
        'on_the_air_tv': on_the_air_tv,
        'form': form,
    }
    # print(popular_movies)
    return render(request, 'home/index.html', context)

def media(request, movie_id):
    # Analytics
    page_view(request)

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            return redirect('/search/{}'.format(form.cleaned_data['search']))
    else:
        form = SearchForm()

    try:
        media = Movie.objects.get(movie_id=movie_id)
    except:
        return HttpResponse(status=404)

    new_view = MovieView(movie_id=movie_id, ip=get_client_ip(request), media_type=media.media_type)
    new_view.save()

    if media.media_type == "movie":
        url = 'https://videospider.in/getvideo?key={}&video_id={}&tmdb=1'.format(player_key, media.movie_id)
        episode_urls = {}
    else:
        url = 'https://streamvideo.link/getvideo?key={}&video_id={}&tmdb=1&tv=1&s=1&e=1'.format(player_key, media.movie_id)

        with urllib.request.urlopen('https://api.themoviedb.org/3/tv/{}?api_key={}&language=en-US'.format(media.movie_id, tmdb_key)) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            seasons = []
            episodes = []
            for i in data["seasons"]:
                seasons.append(i["id"])
                episodes.append(i["episode_count"])

            episode_urls = {}
            c1 = 1
            for i in range(len(seasons)):
                c2 = 1
                for j in range(len(episodes)):
                    episode_url = 'https://streamvideo.link/getvideo?key={}&video_id={}&tmdb=1&tv=1&s={}&e={}'.format(player_key, media.movie_id, c1, c2)
                    episode_tag = 's{}e{}'.format(c1, c2)
                    episode_urls[episode_tag] = episode_url
                    c2 += 1
                c1 += 1

    context = {
        'url': url,
        'media': media,
        'episode_urls': episode_urls,
        'form': form,
    }
    return render(request, 'home/media.html', context)


def search(request, qstr):
    # Analytics
    page_view(request)

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            return redirect('/search/{}'.format(form.cleaned_data['search']))
    else:
        form = SearchForm()

    url = 'https://api.themoviedb.org/3/search/multi?api_key={}&language=en-US&query={}&page=1&include_adult=false'.format(tmdb_key, urllib.parse.quote(qstr))
    result_ids = []

    try:
        req = urllib.request.Request(url = url)
    except Exception as err:
        print(f'Error occurred: {err}')
    else:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            for i in data["results"]:
                result_ids.append(i["id"])
                try:
                    if not Movie.objects.filter(movie_id=i["id"]).exists():
                        if "original_title" in i:
                            with urllib.request.urlopen('https://api.themoviedb.org/3/movie/{}/external_ids?api_key={}'.format(i["id"], tmdb_key)) as resp:
                                data = json.loads(resp.read().decode("utf-8"))
                                imdb_id = data["imdb_id"]
                        elif "original_name" in i:
                            with urllib.request.urlopen('https://api.themoviedb.org/3/tv/{}/external_ids?api_key={}'.format(i["id"], tmdb_key)) as resp:
                                data = json.loads(resp.read().decode("utf-8"))
                                imdb_id = data["imdb_id"]
                        with urllib.request.urlopen('https://www.omdbapi.com?apikey={}&i={}&plot=full'.format(omdb_key, imdb_id)) as resp:
                            data = json.loads(resp.read().decode("utf-8"))
                            rated = data["Rated"]
                            runtime = data["Runtime"]
                            genre = data["Genre"]
                            director = data["Director"]
                            writer = data["Writer"]
                            actors = data["Actors"]
                            plot = data["Plot"]
                            awards = data["Awards"]
                            imdb_rating = data["imdbRating"]
                            media_type = data["Type"]
                        if "original_title" in i:
                            new_movie = Movie(movie_id=i["id"],
                                            imdb_id=imdb_id,
                                            title=i["original_title"],
                                            overview=i["overview"],
                                            popularity=i["popularity"],
                                            poster=i["poster_path"],
                                            release_date=i["release_date"],
                                            language=i["original_language"],
                                            added='',
                                            rated = rated,
                                            runtime = runtime,
                                            genre = genre,
                                            director = director,
                                            writer = writer,
                                            actors = actors,
                                            plot = plot,
                                            awards = awards,
                                            imdb_rating = imdb_rating,
                                            media_type = media_type)
                            new_movie.save()
                        elif "original_name" in i:
                            new_movie = Movie(movie_id=i["id"],
                                            imdb_id=imdb_id,
                                            title=i["original_name"],
                                            overview=i["overview"],
                                            popularity=i["popularity"],
                                            poster=i["poster_path"],
                                            release_date=i["first_air_date"],
                                            language=i["original_language"],
                                            added='',
                                            rated = rated,
                                            runtime = runtime,
                                            genre = genre,
                                            director = director,
                                            writer = writer,
                                            actors = actors,
                                            plot = plot,
                                            awards = awards,
                                            imdb_rating = imdb_rating,
                                            media_type = media_type)
                            new_movie.save()
                except Exception as err:
                    print(err)

    search_results = Movie.objects.filter(movie_id__in=result_ids)

    context = {
        'qstr': qstr,
        'search_results': search_results,
        'form': form
    }
    return render(request, 'home/search.html', context)


def report_a_bug(request):
    # Analytics
    page_view(request)

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            return redirect('/search/{}'.format(form.cleaned_data['search']))
    else:
        form = SearchForm()

    context = {
        'form': form
    }
    return render(request, 'home/report-a-bug.html', context)

def trouble_playing(request):
    # Analytics
    page_view(request)

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            return redirect('/search/{}'.format(form.cleaned_data['search']))
    else:
        form = SearchForm()

    context = {
        'form': form
    }
    return render(request, 'home/trouble-playing.html', context)

def terms(request):
    # Analytics
    page_view(request)

    context = {}
    return render(request, 'home/terms.html', context)

def privacy_policy(request):
    # Analytics
    page_view(request)

    context = {}
    return render(request, 'home/privacy-policy.html', context)