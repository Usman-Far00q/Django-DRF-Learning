from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Album.models import Albums
from Album.serializers import AlbumOutPutSerializer


# Create your views here.

class ViewAlbum(APIView):
    """This is the view that will handle actions related to the Album API-Resource"""

    authentication_classes = [TokenAuthentication]  # We will be using Django's Bsic
    # Token Authentification for the resources in this endpoint
    # please note that the token is to be sent inside the HTTP_HEADER=Authorization with the pattern Token <Token here>

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """View All albums in the DB"""

        # because of the authentication_classes set on this endpoint,
        # we can now safely see request.user attr (this attr is automatically set by the contrib.auth middleware that comes baked intp django)
        album_qs = Albums.objects.all()
        album_rest_dict = AlbumOutPutSerializer(album_qs, many=True)
        return Response(album_rest_dict.data)
