from rest_framework import serializers

from Artist.serializers import ArtistOutPutSerializer
from Song.models import Songs


class SongOutPutSerializer(serializers.ModelSerializer):
    # I declared ArtistOutPutSerializer(many=True), with attr=many to be =True,
    # because in sung_by_artists = ArtistOutPutSerializer(many=True), the
    # Song.sung_by_artists is a query_set and NOT a single Artist Obj
    sung_by_artists = ArtistOutPutSerializer(many=True)  # Here we are using another Serializer (specifically the=ArtistOutPutSerializer)
    # within this SongOutPutSerializer, when we use one serializer in another, we are "Nesting Serializers",
    # WE ALWAYS HAVE TO BE CAREFUL when naming the field_name of a nested serializer (we named it "sung_by_artists", over here), We
    # could NOT name it anything else other than "sung_by_artists", because the wrapper serializer (aka=SongOutPutSerializer, aka the
    # serializer that nests another serializer), is based on
    # the Model=Songs (u can confirm this by looking at what
    # value is given to attr=model, for the sub-class=Meta), and since inside the
    # models.py file for the Songs we have given the name="sung_by_artists" to the "reverse_lookup" field (u can confirm this by seeing the
    # code snippet --> sung_by_artists = models.ManyToManyField(<Blah..Blah..Blah...>)), hence the field_name for the nested serializer has to be "sung_by_artists"

    # Summary of the above:
    # the field name given to a nested serializer has to be --> the "reverse lookup" name that
    # would give you the model instance for which the nested serializer is made for

    class Meta:
        model = Songs
        fields = ["name", "rating", "sung_by_artists"]  # the field "sung_by_artists"
        # is going to be an Array of Artist Objs, instead of a SINGULAR Artist Obj because of the
        # "many-to-many" cardinality of the "Song <--> Artist" relation
