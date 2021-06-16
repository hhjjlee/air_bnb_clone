from django.contrib import admin
from . import models

""" List Admin Definition """


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    pass
