from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artists/', include('Artist.urls')),
    path('albums/', include('Album.urls')),
    path('gimme-token', views.obtain_auth_token),
    path('songs/', include('Song.urls')),
]
