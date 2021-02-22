from django.contrib import admin

from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'language', 'popularity')

admin.site.register(Movie, MovieAdmin)