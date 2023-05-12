from django.contrib import admin

from config.models import Config


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'value',)
    list_editable = ["value", ]
