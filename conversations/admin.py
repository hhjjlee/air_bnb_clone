from django.contrib import admin
from . import models

""" Message Admin Definition """


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    pass


"""  Conversation Admin Definition """


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    pass
