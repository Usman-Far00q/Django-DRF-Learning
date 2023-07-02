from django.db import models

from Artist.models import Artists


# Create your models here.
class Albums(models.Model):
    class Meta:
        db_table = "Albums"

    released_by = models.OneToOneField(
        Artists,
        related_name="made_album",  # If you do not specify the related_name argument for the OneToOneField,
        # Django will use the lowercase name of the current model as default value.

        on_delete=models.SET_DEFAULT,  # I could also have used just models.SET_NULL
        # (instead of setting the "on_delete" AND "default" route ) ....  btw this option lets you control
        # what would happen to a specific Album entity, if the
        # Artist_entity (that the aforementioned specific Album
        # entity's released_by field points to) is deleted

        default=None,  # I am setting a default value for this field just because
        # I have passed SRT_DEFAULT option to its on_delete param
        null=True,  # I have to do it cuz of the fact that on_delete rule that I have made on this field will cause this field to possibly contains NULL

        blank=True  # Am setting this so that I can Add an Album via Django-Admin without giving a value to this field
    )
    name = models.CharField(max_length=30, blank=False)
