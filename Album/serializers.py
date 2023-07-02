from rest_framework import serializers

from Album.models import Albums
from Artist.serializers import ArtistOutPutSerializer


class AlbumOutPutSerializer(serializers.ModelSerializer):
    released_by = ArtistOutPutSerializer()  # Here we are using another Serializer (specifically the=ArtistOutPutSerializer)
    # within this AlbumOutPutSerializer, when we use one serializer in another, we are "Nesting Serializers",
    # WE ALWAYS HAVE TO BE CAREFUL when naming the field_name of a nested serializer (we named it "released_by", over here), We
    # could NOT name it anything else other than "released_by", because the wrapper serializer (aka=AlbumOutPutSerializer, aka the
    # serializer that nests another serializer), is based on
    # the Model=Albums (u can confirm this by looking at what
    # value is given to attr=model, for the sub-class=Meta), and since inside the
    # models.py file for the Album we have given the name="released_by" to the "reverse_lookup" field (u can confirm this by seeing the
    # code snippet --> released_by = models.OneToOneField(<Blah..Blah..Blah...>)), hence the field_name for the nested serializer has to be "released_by"

    # Summary of the above:
    # the field name given to a nested serializer has to be --> the "reverse lookup" name that
    # would give you the model instance for which the nested serializer is made for

    class Meta:
        model = Albums
        fields = ["name", "released_by"]
