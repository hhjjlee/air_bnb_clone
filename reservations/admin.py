from django.contrib import admin
from . import models

""" Reservatrion admin Definition """


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass
