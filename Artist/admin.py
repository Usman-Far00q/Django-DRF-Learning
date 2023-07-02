from django.contrib import admin

from Artist.models import Artists

# Register your models here.

# ----------------------------------------------------------------------------------
# # This can be enough for us if we only want to play and display
# # the Artists Table and its Data to be displayed in the Django-Admin Panel,
# admin.site.register(Artists)
# --------------------------------------------------------------

# if we want finer control of stuff like:
# 1 - How the Table should be displayed inside the Django-admin Panel
# 2- How do we want certain columns of the Table to be read_only and Not let people change them via the Admin-Panel
# 3- How do we want the Contents of the table to be displayed (sorted? not sorted? random, etc)

# if we want such fine grain control then we will have to make a child class of cls="Modeldmin", where we will
# set certain configurations regarding the --> model <---> Django-Admin Panel, I like to call this class as an "Admin-model configuration class"
# and then register the model to the django-admin-panel along with the models aforementioned " Admin-model configuration class"

# for "Admin-model configuration class" it is recommended we follow the nomenclature=<model_name>Admin


class ArtistsAdmin(admin.ModelAdmin):
    list_display = ("first_name", "age")


admin.site.register(Artists, ArtistsAdmin)



