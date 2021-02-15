from django.db import models

class Movie(models.Model):
    movie_id = models.CharField(max_length=128)
    imdb_id = models.CharField(max_length=128, blank=True, null=True)
    title = models.CharField(max_length=128)
    overview = models.CharField(max_length=512)
    popularity = models.CharField(max_length=128)
    poster = models.CharField(max_length=128, null=True, blank=True)
    release_date = models.CharField(max_length=128)
    language = models.CharField(max_length=128)
    added = models.CharField(max_length=128, blank=True, null=True)
    rated = models.CharField(max_length=128, blank=True, null=True)
    runtime = models.CharField(max_length=128, blank=True, null=True)
    genre = models.CharField(max_length=128, blank=True, null=True)
    director = models.CharField(max_length=128, blank=True, null=True)
    writer = models.CharField(max_length=128, blank=True, null=True)
    actors = models.CharField(max_length=128, blank=True, null=True)
    plot = models.CharField(max_length=128, blank=True, null=True)
    awards = models.CharField(max_length=128, blank=True, null=True)
    imdb_rating = models.CharField(max_length=128, blank=True, null=True)
    media_type = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
