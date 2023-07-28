from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from Artist.models import Artists


# Create your models here.
class Songs(models.Model):
    class Meta:
        db_table = "Songs"
        verbose_name_plural = 'DjangoAdmin_panel_mai_Songs'  # when you register this Model
        # inside the Django Admin Panel, this is the name that This Model will be shown with over their

    # the attr name=sung_by_artists below and the cardinality of the relation aka Many-to-Many,
    # will cause Django to mae the Songs<-->Artists pivot-table with the name
    # <Class_name>_<many-to-many_attr_name> which in this case will be Songs_sung_by_artists
    sung_by_artists = models.ManyToManyField(
        Artists,
        related_name="sang_songs",  # If you do not specify the related_name argument for the ManyToManyField,
        # Django will use the <lowercase name of the current model>_set as default value ... so it would be then
        # Artists.songs_set.all() instead of Artists.sang_songs.all().

        # on_delete=models.CASCADE # this attr is NOT applicable on ManyToManyField

        # null=True,  # this attr is NOT applicable on ManyToManyField

        blank=False  # I Am setting this so that I can NOT Add a Song via Django-Admin without giving a value
        # to this "sung_by_artists" field, aka a song can only exist if the Artist(s) that sung it also exist
    )
    name = models.CharField(max_length=30, blank=False)
    rating = models.IntegerField(null=False,
                                 blank=False,
                                 default=5.0,
                                 validators=[MaxValueValidator(10), MinValueValidator(1)]
                                 )  # A song's rating has to be within the limits [1-10]

    def __str__(self):
        """This method is simple Python behaviour, this is
        shown whenever the Object of this Class is
        printed in a console, etc (Django uses it in the same way as well)"""
        return f'{self.name}-SONG'

