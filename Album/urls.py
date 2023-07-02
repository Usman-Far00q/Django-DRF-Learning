from django.urls import path, include

from Album.views import ViewAlbum

urlpatterns = [
    path('', ViewAlbum.as_view())
    ]
