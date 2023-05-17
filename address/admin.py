from django.contrib import admin

from address.models import  Country


# Register your models here


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_editable = ["name", ]
    list_display_links = None
