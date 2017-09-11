from django.contrib import admin
from .models import Song, Chat, Tracker, Response, Player

admin.site.register(Song)
admin.site.register(Chat)
admin.site.register(Tracker)
admin.site.register(Response)
admin.site.register(Player)
