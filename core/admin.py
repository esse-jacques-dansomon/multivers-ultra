from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin
from import_export.admin import ImportExportModelAdmin

from core.models import Level, Category, Skill, Country, Developer, Config, Status, DeveloperSkill, Address


@admin.register(Level)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_editable = ["name", ]
    list_display_links = None


@admin.register(Category)
class KindAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_editable = ["name", ]
    list_display_links = None


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_editable = ["name", ]
    list_display_links = None


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_editable = ["name", ]
    list_display_links = None


@admin.register(Developer)
class DeveloperAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
    search_fields = ('skills__name',)
    list_display = ('name', 'email', 'phone', 'address', 'status', 'competences', 'created_at', 'updated_at')
    list_editable = ["email", "status", ]
    readonly_fields = ('created_at', 'updated_at')

    def competences(self, obj):
        #competence with level and experience
        return DeveloperSkill.objects.filter(developer=obj).values_list('skill__name', 'level__name', 'experience')


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'value',)
    list_editable = ["value", ]


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'code',)
    list_editable = ["code", ]


@admin.register(DeveloperSkill)
class DeveloperSkillAdmin(admin.ModelAdmin):
    list_display = ('developer', 'skill', 'level', 'experience')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'street', 'country')
    list_editable = ["city", "street", "country"]
