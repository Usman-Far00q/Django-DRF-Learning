from django.urls import path, include

from Artist.views import ViewArtist

urlpatterns = [
    path('', ViewArtist.as_view())
    ]
