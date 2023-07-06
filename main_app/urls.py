from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('games/', views.GameList.as_view(), name="game_list"),
    path('games/new', views.GameCreate.as_view(), name="game_create"),
    # Our new Route including the pk param
    path('games/<int:pk>/', views.GameDetail.as_view(), name="game_detail"),
    path('games/<int:pk>/update',views.GameUpdate.as_view(), name="game_update"),
    path('games/<int:pk>/delete',views.GameDelete.as_view(), name="game_delete"),
    path('games/<int:pk>/characters/new/', views.CharacterCreate.as_view(), name="character_create"),
    path('playlists/<int:pk>/characters/<int:character_pk>/', views.PlaylistCharacterAssoc.as_view(), name="playlist_character_assoc"),
]

 
