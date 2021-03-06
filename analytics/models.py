from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

class ClientConnection(models.Model):
    ip = models.CharField(max_length=50, default="xxx", blank=True, null=True)
    url = models.CharField(max_length=512, default="xxx", blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    request_body = models.TextField(blank=True, null=True)
    country_code = models.CharField(max_length=512, blank=True, null=True)
    country_name = models.CharField(max_length=512, blank=True, null=True)
    region_code = models.CharField(max_length=512, blank=True, null=True)
    region_name = models.CharField(max_length=512, blank=True, null=True)
    city = models.CharField(max_length=512, blank=True, null=True)
    zip_code = models.CharField(max_length=512, blank=True, null=True)
    latitude = models.CharField(max_length=512, blank=True, null=True)
    longitude = models.CharField(max_length=512, blank=True, null=True)
    metro_code = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return str(self.ip)

    class Meta:
        verbose_name = "Client Connection"
        verbose_name_plural = "Client Connections"

    @property
    def title(self):
        return str(self.ip)

# idk why tf i made these two seperate models, but now i'm too lazy to change
class UserClientConnection(models.Model):
    ip = models.CharField(max_length=50, default="xxx", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    url = models.CharField(max_length=512, default="xxx", blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    request_body = models.TextField(blank=True, null=True)
    country_code = models.CharField(max_length=512, blank=True, null=True)
    country_name = models.CharField(max_length=512, blank=True, null=True)
    region_code = models.CharField(max_length=512, blank=True, null=True)
    region_name = models.CharField(max_length=512, blank=True, null=True)
    city = models.CharField(max_length=512, blank=True, null=True)
    zip_code = models.CharField(max_length=512, blank=True, null=True)
    latitude = models.CharField(max_length=512, blank=True, null=True)
    longitude = models.CharField(max_length=512, blank=True, null=True)
    metro_code = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return str(self.ip)

    class Meta:
        verbose_name = "User Client Connection"
        verbose_name_plural = "User Client Connections"

    @property
    def title(self):
        return str(self.ip)

class MovieView(models.Model):
    ip = models.CharField(max_length=50, default="xxx", blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    movie_id = models.CharField(max_length=512)
    media_type = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = "Movie View"
        verbose_name_plural = "Movie Views"

    @property
    def title(self):
        return str(self.ip)