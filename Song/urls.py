from django.urls import path

from Song.views import ViewSong

urlpatterns = [
    path('', ViewSong.as_view())
    ]
