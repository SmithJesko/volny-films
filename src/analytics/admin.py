from django.contrib import admin

from .models import ClientConnection, UserClientConnection, MovieView

admin.site.register(ClientConnection)
admin.site.register(UserClientConnection)
admin.site.register(MovieView)
