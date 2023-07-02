from django.db import models


# Create your models here.
class Artists(models.Model):
    class Meta:
        db_table = "the_artists"  # the name of the Table this model will represent inside the SQL DB
        verbose_name_plural = 'Django_admin_panel_mai_artists'  # when you register this Model
        # inside the Django Admin Panel, this is the name that This Model will be shown with over their

    first_name = models.CharField(max_length=30, blank=False)

    last_name = models.CharField(max_length=30, blank=False)  # notice how since we will not be mentioning this field inside
    # the ArtistInPutSerializer's Meta Class's Field attr, validation won't actually
    # check if this last_name is provided in a POST request OR NOT (moral of the story ==> a Serializer is only
    # going to validate data that you tell are to be validated)

    stage_name = models.CharField(max_length=30, blank=True)
    age = models.IntegerField()

    # when null == False this mean that the DB can not have a NULL value in it for that Field,
    # when Blank == false, this means that this Field is NOT needed inside the POST request, BUT it migth
    # mean that this field is needed to be NOT NULL in the DB (this DB stuff is determined by the value you passed to the null arg)

    def __str__(self):
        """This method is simple Python behaviour, this is
        shown whenever the Object of this Class is
        printed in a console, etc (Django uses it in the same way as well)"""
        return f'{self.first_name}-ARTIST'
