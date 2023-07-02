from typing import OrderedDict

from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ApnaAuth.authenticate import ApnaAuthentication
from Artist.models import Artists
from Artist.serializers import ArtistOutPutSerializer, ArtistInPutSerializer


# Create your views here.
class ViewArtist(APIView):
    """This is the view that will handle actions related to the Artist API-Resource"""

    authentication_classes = [ApnaAuthentication]  # I am using my Custom Django Authentication in this endpoint

    permission_classes = [IsAuthenticated]

    # all the request handler methods below can access request.user attr,
    # (this attr is automatically set by the contrib.auth middleware that comes baked into django)...
    # the middleware=contrib.auth calls a method=authenticate()
    # (BEFORE invoking the appropriate request handler methods defined below)
    # of the ApnaAuthentication Class I have made, using that it gets what to save inside request.user attr

    # queryset = Artists.objects.all()

    def get(self, request):
        """Return a list of all Artists."""
        artists_qs = Artists.objects.all()
        artists_rest_dict = ArtistOutPutSerializer(artists_qs, many=True)
        return Response(artists_rest_dict.data)

    def post(self, request):
        """Create An Artist"""
        data_to_make_artist_from = request.data
        data_serializer = ArtistInPutSerializer(data=data_to_make_artist_from)

        # DRF enforces data validation in the deserialization process,
        # which is why you need to call is_valid() before accessing the validated data.
        # If the data is invalid, errors are then appended to
        # the serializer's error property and a ValidationError is thrown.
        if data_serializer.is_valid(raise_exception=True):
            # just a side note --> You cannot call `.save()` after
            # accessing `serializer.data`.If you need to
            # access data before committing to the database then inspect 'serializer.validated_data' instead.
            data_serializer.save()  # create() method of the serializer will be called now
            validated_data_dict = data_serializer.validated_data
            return Response(data=validated_data_dict, status=200)

    def put(self, request):
        """Update an already existing Artist's Data"""
        data_to_modify_artists_with = request.data
        id_of_artist_to_modify = request.data.get("id", None)
        try:
            artist_db_instance = Artists.objects.get(id=id_of_artist_to_modify)
        except Artists.DoesNotExist:
            return Response(data={"Artist with that ID does NOT exist"}, status=404)

        data_to_modify_artists_with['garbage_key'] = 'garbage_value'  # this key:val will not even be analyzed
        # for validation, and won't be in the validated_data attr of the serializer

        artist_serializer = ArtistInPutSerializer(artist_db_instance, data=data_to_modify_artists_with, many=False)
        if artist_serializer.is_valid(raise_exception=True):
            artist_serializer.save()  # create() method of the serializer won't be
            # called this time, instead update() method wil be called,
            # since you instantiated the serializer like so=ArtistInPutSerializer(instance, data, many), INSTEAD of ArtistInPutSerializer(data, many)
        data: OrderedDict = artist_serializer.validated_data

        return Response(data=data, status=200)
