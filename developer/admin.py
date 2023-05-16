from django.contrib import admin
from django.contrib.admin import RelatedFieldListFilter
from django_admin_multi_select_filter.filters import MultiSelectFieldListFilter
from djangoql.admin import DjangoQLSearchMixin
from import_export.admin import ImportExportModelAdmin

from developer.models import Developer, DeveloperSkill, Status, Level, Language


class DeveloperSkillInline(admin.TabularInline):
    model = DeveloperSkill
    extra = 1




# Register your models here.
@admin.register(Developer)
class DeveloperAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
    search_fields = ('name',)
    list_display = ('avatar', 'nom', 'prenom', 'langues', 'whatsapp', 'address', 'competences', 'tjm')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = (
        ('status__name', MultiSelectFieldListFilter),
        ('address__country__name', MultiSelectFieldListFilter),
        ('skills__name', MultiSelectFieldListFilter),
        ('skills__category__name', MultiSelectFieldListFilter),
        ('developer_skills__level__name', MultiSelectFieldListFilter),
        'sex',
    )
    inlines = [DeveloperSkillInline]

    def competences(self, obj):
        # transform to str competence with level and experience
        return ', '.join([f'{devSkill}' for devSkill in DeveloperSkill.objects.filter(developer=obj)])

    def langues(self, obj):
        # transform to str competence with level and experience
        return ', '.join([f'{langue}' for langue in Language.objects.filter(developer=obj)])

    def prenom(self, obj):
        return obj.firstName

    def nom(self, obj):
        return obj.lastName

    def avatar(self, obj):
        # create hmtl for the photo
        return f'<img src="{obj.photo.url}" width="50" height="50" />'

    def whatsapp(self, obj):
        # https://wa.me/22507070707
        return f'https://wa.me/{obj.whatsApp}' if obj.whatsApp else None

    def email(self, obj):
        # mailto:email
        return f'mailto:{obj.email}' if obj.email else None

    def tel(self, obj):
        # phone:tel
        return f'phone:{obj.phone}' if obj.phone else None


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'order',)
    list_editable = ["name", 'order']
    list_display_links = None


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'isDefault',)
    list_editable = ["isDefault", ]
