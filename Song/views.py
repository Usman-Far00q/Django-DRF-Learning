from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from Song.models import Songs
from Song.serializers import SongOutPutSerializer


# Create your views here.
class ViewSong(APIView):
    """This is the view that will handle actions related to the Songs API-Resource"""

    def get(self, request):
        """View All Songs in the DB"""
        song_qs = Songs.objects.all()
        song_result_dict = SongOutPutSerializer(song_qs, many=True)
        return Response(song_result_dict.data)
