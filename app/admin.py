from django.contrib import admin
from app import models

# Register your models here.


@admin.register(models.Slot)
class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_free', 'username']
