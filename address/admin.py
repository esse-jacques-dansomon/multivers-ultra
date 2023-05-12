from django.contrib import admin

from address.models import Address, Country


# Register your models here.
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'street', 'country')
    list_editable = ["city", "street", "country"]


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_editable = ["name", ]
    list_display_links = None
