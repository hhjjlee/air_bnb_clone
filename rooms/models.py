from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
# from users import models as user_models

""" Abstract Item """


class AbstractItem(core_models.TimeStampedModel):
    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


""" RoomType Model Definition """


class RoomType(AbstractItem):
    # pass
    class Meta:
        verbose_name = "Room Type"
        ordering = ["name"]


"""amenity Object Definition """


class Amenity(AbstractItem):
    # pass
    class Meta:
        verbose_name_plural = "Amenites"


"""Facility Object Definition """


class Facility(AbstractItem):
   # pass
    class Meta:
        verbose_name_plural = "Facilities"


"""Rule Object Definition """

""" HouseRule Model Definition """


class HouseRule(AbstractItem):
    pass

    class Meta:
        verbose_name = "House Rule"


""" Photo Model Definition """


class Photo(core_models.TimeStampedModel):
    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


"""Room Model Definition """


class Room(core_models.TimeStampedModel):

    name = models.CharField(max_length=140)
    description = models.TextField()
    counties = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey(
        "RoomType", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField("Amenity", blank=True)
    facilities = models.ManyToManyField("Facility", blank=True)
    house_rules = models.ManyToManyField("HouseRule", blank=True)

    def __str__(self):
        return self.name
