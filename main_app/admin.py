from django.contrib import admin
from .models import Game, Character, Playlist # import the Artist model from models.py
# Register your models here.

admin.site.register(Game) # this line will add the model to the admin panel
admin.site.register(Character)
admin.site.register(Playlist)