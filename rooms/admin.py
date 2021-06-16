from django.contrib import admin
from . import models

# Register your models here.


""" Item admin Definition """


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmind(admin.ModelAdmin):
    pass


"""Room Admin Definition """


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )

    list_filter = ("instant_book", "city", "country")

    search_fields = ("=city", "^host__username")


"""PhotoAdmin Admin Definition """


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
