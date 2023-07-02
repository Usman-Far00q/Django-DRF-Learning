from typing import Dict

from rest_framework import serializers

from Artist.models import Artists


class ArtistOutPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        fields = ['stage_name', 'age']


class ArtistInPutSerializer(serializers.ModelSerializer):
    valid_stage_name = serializers.SerializerMethodField(read_only=True)

    # the method=get_valid_stage_name below is called when we call the .data attr of a ArtistInPutSerializer instance
    # ALso not how it follows the get_<method_field_attr_Name> nomenclature
    def get_valid_stage_name(self, obj: Dict):  # if this were an Output serializer
        # (aka the one where we give a qs (query-set) instead of data when
        # initializing the Serializer Obj) , the obj arg
        # would have been the instance aka row of a Model

        if "stage_name" in obj:
            return obj['stage_name']
        else:
            # Since the Artists Model dictates that the field=stage_name can be left blank,
            # but we want our DB to have a stage name
            # field to be NOT NULL, hence we make one using the
            # first_name (first_name is a Must according to the
            # Artists Model, hence is_valid() method of the
            # serializer will fail if first_name isn't provided, hence
            # our assumption here is always going to work)
            return obj['first_name'] + "_PERFORMER"

    class Meta:
        model = Artists
        fields = ['first_name', 'valid_stage_name', 'age', 'stage_name']  # for an Artist to be created,
        # ALL these fields must be provided (unless told otherwise inside the models.py file where these Fields are actually defined),
        # this now obviously means valid_stage_name is something that SHOULD Never be provided since it is never inside a model.py file

    # the method=validate_age will be called when .is_valid() is
    # called on the Serializers instance, AND iff "age" is a part of the validated_data, aka
    # the data being passed inside the data arg when instantiation the Serializer object in the first place
    # ALso note that the method name needs to follow Django's validate_<attr_name> nomenclature
    def validate_age(self, value):
        if value <= 0:
            raise serializers.ValidationError("An Artist's age can not be less than or equal to zero")
        return value

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
        if "stage_name" not in validated_data:
            return Artists.objects.create(**validated_data, stage_name=self.data["valid_stage_name"])
        else:
            return Artists.objects.create(**validated_data)

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



