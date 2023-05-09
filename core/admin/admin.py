from django.contrib import admin

from core.models.models import Languages, Kind, Developer


@admin.register(Languages)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Kind)
class KindAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'name', 'site', 'mail', 'page', 'phone', 'whatApps')
    list_editable = ["mail", ]
    readonly_fields = ('created_at', 'updated_at')

# # Register your models here.
# @admin.register(Developer)
# class DeveloperAdmin(DjangoQLSearchMixin,ImportExportModelAdmin ):
#     search_fields = ('languages',)
#     list_display = ('firstname', 'name', 'site', 'mail', 'page', 'phone', 'whatApps')
#     list_editable = ["mail", ]
#     readonly_fields = ('created_at', 'updated_at')
