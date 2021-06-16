from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


""" Custom User Admin """


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    pass
