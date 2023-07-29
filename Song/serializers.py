from typing import Dict, List

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from Artist.models import Artists
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


class SongInPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ['name_of_artists', 'name']  # for a Song to be created,
        # ALL these fields must be provided (unless told otherwise inside the models.py file where these Fields are actually defined),
        # this now obviously means name_of_artists is something that will NEVER be a "MUST to provide" because
        # it is not mentioned inside the models.py file, BUT because we set required=True
        # in name_of_artists = serializers.ListField(required=True).. now name_of_artists IS
        # a "MUST to provide" key in request JSON

    name_of_artists = serializers.ListField(required=True)  # required=True validates/forces name_of_artists be sent all the time by user JSON request

    # def validate_name_of_artists is called by is_valid > run_validations > to_internal_value
    # note the validate_<field_name> nomenclature
    def validate_name_of_artists(self, value: List) -> List[Artists]:
        artists_found = []
        for artist in value:
            try:
                an_artist = Artists.objects.get(first_name=artist)
            except ObjectDoesNotExist as DoesNotExist:
                raise serializers.ValidationError(f"An artist with the name={artist} does not exist")
            artists_found.append(an_artist)
        return value  # e are returning back List of str instead of List of Artist Objs
        # because we want self.validated_data["name_of_artists"] to be List of str instead of List of Artists
        # because all custom-attrs of a InputSerializer should be of Python primitive Types

    # this method below is called iff both the conditions are fulfilled:
    # Condition-1) we instantiated the Serializer like so=ArtistInPutSerializer(data=data, many=<BOOL>)
    # Condition-2) we called the .save method on the aforementioned Serializer instance
    # and all this method will do is that it will create a new instance inside the DB.
    def create(self, validated_data: Dict):
        # remember the "validated_data" attr of the Serializer object contains whatever we list inside the "fields" attr of the Meta sub-Class
        # that we define inside the Serializer **SET-INTERSECT** the stuff we pass to the data param when
        # instantiating the serializers, and once that Data has
        # successfully passed through the appropriate validators
        # that have been written for those attributes of the Serializer

        # whereas the "data" is the stuff we pass to the data param when
        # instantiating the serializers, and once that Data has
        # successfully passed through the appropriate validators
        # that have been written for those attributes of the Serializer **SET-UNION** whatever we list inside the "fields" attr of the Meta sub-Class
        # that we define inside the Serializer
        song_to_create = Songs(name=validated_data['name'], rating=3.0)
        song_to_create.save()
        artists_names = validated_data["name_of_artists"]  # depends on what def validate_name_of_artists returns
        for artist_name in artists_names:
            an_artist = Artists.objects.get(first_name=artist_name)
            song_to_create.sung_by_artists.add(an_artist)
        return song_to_create

    # th "update" method below is called iff both the conditions are fulfilled:
    # Condition-1) we instantiated the Serializer like so=ArtistInPutSerializer(Artist_instance, data=data, many=False)
    # Condition-2) we called the .save method on the aforementioned Serializer instance
    # and all this method will do is that it will update an existing instance inside the DB.
    def update(self, instance: Artists, validated_data: Dict):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.stage_name = validated_data.get('stage_name', instance.stage_name)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance

    # # def validate is called at the very end of validation process
    # def validate(self, data):
    #     raise serializers.ValidationError("<Blah blah Blah>")
