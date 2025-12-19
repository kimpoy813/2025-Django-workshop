from django.contrib import admin
from . import models

@admin.register(models.Guest)
class GuestAdmin(admin.ModelAdmin):
	list_display = ("id",)