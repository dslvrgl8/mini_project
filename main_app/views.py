#...
# This will import the class we are extending 
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
# import models
from .models import Game, Character, Playlist
# after our other imports 
from django.views.generic import DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["playlists"] = Playlist.objects.all()
        return context

    #...
class About(TemplateView):
    template_name = "about.html"

class GameList(TemplateView):
    template_name = "game_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["games"] = Game.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["games"] = Game.objects.all()
            # default header for not searching 
            context["header"] = "Top Games"
        return context
    
class GameCreate(CreateView):
    model = Game
    fields = ['name', 'img', 'bio', 'verified_game']
    template_name = "game_create.html"
    def get_success_url(self):
        return reverse('game_detail', kwargs={'pk': self.object.pk})

class GameDetail(DetailView):
    model = Game
    template_name = "game_detail.html"

class GameUpdate(UpdateView):
    model = Game
    fields = ['name', 'img', 'bio', 'verified_game']
    template_name = "game_update.html"
    def get_success_url(self):
        return reverse('game_detail', kwargs={'pk': self.object.pk})

class GameDelete(DeleteView):
    model = Game
    template_name = "game_delete_confirmation.html"
    success_url = "/games/"

class CharacterCreate(View):

    def post(self, request, pk):
        title = request.POST.get("title")
        length = request.POST.get("length")
        game = Game.objects.get(pk=pk)
        Character.objects.create(title=title, length=length, artist=game)
        return redirect('game_detail', pk=pk)
    
class PlaylistCharacterAssoc(View):

    def get(self, request, pk, character_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the playlist by the id and
            # remove from the join table the given song_id
            Playlist.objects.get(pk=pk).characters.remove(character_pk)
        if assoc == "add":
            # get the playlist by the id and
            # add to the join table the given song_id
            Playlist.objects.get(pk=pk).characters.add(character_pk)
        return redirect('home')
    
class GameDetail(DetailView):
    model = Game
    template_name = "game_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["playlists"] = Playlist.objects.all()
        return context





# class Game:
#     def __init__(self, name, image, bio):
#         self.name = name
#         self.image = image
#         self.bio = bio

# games = [
#     Game("Diablo 4", "https://i.guim.co.uk/img/media/d6f9328516375ad80199c91c31d02d2413852dea/0_347_12000_7200/master/12000.jpg?width=1200&quality=85&auto=format&fit=max&s=41f0291e38d64ee1f8ea224177ecad74", "action beat-em-up, fight god and the devil"), Game("Tears of the Kingdom", "https://assets-prd.ignimgs.com/2022/09/14/zelda-tears-of-the-kingdom-button-2k-1663127818777.jpg", "Newest Legend of Zelda game, open world, lose hours of your life"), Game("Street Fighter 6", "https://cdn.cloudflare.steamstatic.com/steam/apps/1364780/capsule_616x353.jpg?t=1686291121", "Newest entry in the figthing game world"),
# ]
