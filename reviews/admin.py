from django.contrib import admin
from . import models
# Register your models here.

""" Review Admin Definiton """


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
