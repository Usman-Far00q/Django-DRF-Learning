from django.contrib import admin

from Song.models import Songs


# Register your models here.
class SongsAdmin(admin.ModelAdmin):
    list_display = ("name", "rating")


admin.site.register(Songs, SongsAdmin)
