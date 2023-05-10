from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin
from import_export.admin import ImportExportModelAdmin

from core.models import Level, Category, Skill, Country, Developer


@admin.register(Level)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Category)
class KindAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Country)
class NiveauAdmin(admin.ModelAdmin):
    list_display = ('name',)


# Register your models here.
@admin.register(Developer)
class DeveloperAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
    search_fields = ('skills', )
    list_display = ('name', 'email', 'phone', 'address', 'created_at', 'updated_at')
    list_editable = ["email", ]
    readonly_fields = ('created_at', 'updated_at')
