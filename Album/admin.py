from django.contrib import admin

from Album.models import Albums


from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']

# Register your models here.


class AlbumsAdmin(admin.ModelAdmin):
    list_display = ("name", "released_by")


admin.site.register(Albums, AlbumsAdmin)

