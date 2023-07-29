from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from Song.models import Songs
from Song.serializers import SongOutPutSerializer, SongInPutSerializer


# Create your views here.
class ViewSong(APIView):
    """This is the view that will handle actions related to the Songs API-Resource"""

    def get(self, request):
        """View All Songs in the DB"""
        song_qs = Songs.objects.all()
        song_result_dict = SongOutPutSerializer(song_qs, many=True)
        return Response(song_result_dict.data)

    def post(self, request):
        """Create A Song"""
        data_to_make_song_from = request.data
        data_serializer = SongInPutSerializer(data=data_to_make_song_from)

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
            return Response(data=validated_data_dict, status=200, exception=True)
