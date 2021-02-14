from django.db import models

class Movie(models.Model):
    movie_id = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    overview = models.CharField(max_length=512)
    popularity = models.CharField(max_length=128)
    poster = models.CharField(max_length=128, null=True, blank=True)
    release_date = models.CharField(max_length=128)
    language = models.CharField(max_length=128)
    media_type = models.CharField(max_length=128, blank=True, null=True)
    added = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.title