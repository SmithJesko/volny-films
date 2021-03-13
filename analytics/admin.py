from django.contrib import admin

from .models import ClientConnection, UserClientConnection, MovieView

class UserClientConnectionAdmin(admin.ModelAdmin):
    list_display = ('ip', 'url', 'user', 'region_code', 'country_code', 'timestamp')

class ClientConnectionAdmin(admin.ModelAdmin):
    list_display = ('ip', 'url', 'region_code', 'country_code', 'timestamp')

admin.site.register(UserClientConnection, UserClientConnectionAdmin)
admin.site.register(ClientConnection, ClientConnectionAdmin)
admin.site.register(MovieView)
