from django.contrib import admin
from django.utils.html import format_html
from django_admin_multi_select_filter.filters import MultiSelectFieldListFilter
from djangoql.admin import DjangoQLSearchMixin
from import_export.admin import ImportExportModelAdmin

from developer.models import Developer, DeveloperSkill, Status, Level, Language, Experience


class DeveloperSkillInline(admin.TabularInline):
    model = DeveloperSkill
    extra = 1


class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 1


# Register your models here.
@admin.register(Developer)
class DeveloperAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
    search_fields = ('name',)
    list_display = ('avatar', 'nom', 'tel', 'mail', 'whatsapp', 'langues', 'addresse', 'competences', 'tjm')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = (
        ('status__name', MultiSelectFieldListFilter),
        ('country__name', MultiSelectFieldListFilter),
        ('developer_skills__skill__name', MultiSelectFieldListFilter),
        ('developer_skills__skill__category__name', MultiSelectFieldListFilter),
        ('developer_skills__level__name', MultiSelectFieldListFilter),
        'sexe',
    )
    fieldsets = (
        ('Informations personnelles', {
            'classes': ('collapse',),
            'fields': ('name', 'firstName', 'sexe', 'phone', 'email', 'fixTel', 'address', 'country')
        }),
        ('Fichiers', {
            'classes': ('collapse',),
            'fields': ('cv', 'photo', 'video')
        }),
        ('Réseaux sociaux', {
            'classes': ('collapse',),
            'fields': (
                'whatsApp', 'otherCanal', 'linkedin', 'instagram', 'facebook', 'github', 'gitlab', 'bitbucket',
                'website')
        }),
        ('Tarification', {
            'classes': ('collapse',),
            'fields': ('tjm', 'devise', 'modeReglement', 'bankAccount')
        }),
        ('Autres informations', {
            'classes': ('collapse',),
            'fields': ('status', 'languages', 'annotations', 'availability')
        }),

    )
    inlines = [DeveloperSkillInline, ExperienceInline]

    def competences(self, obj):
        # Get DeveloperSkill objects for the developer
        dev_skills = DeveloperSkill.objects.filter(developer=obj)

        # Generate the string representation for each DeveloperSkill
        competence_strings = []
        for dev_skill in dev_skills:
            competence_strings.append(
                f'{dev_skill.skill} - Level: {dev_skill.level}, Experience: {dev_skill.experience} ans')

        # Join the competence strings with new lines
        return ',\n'.join(competence_strings)

    def langues(self, obj):
        # transform to str competence with level and experience
        return ', '.join([f'{langue}' for langue in Language.objects.filter(developer=obj)])

    def nom(self, obj):
        return obj.name + ' ' + obj.firstName

    def avatar(self, obj):
        if obj.photo:
            return format_html('<img src="{}" alt="Avatar" style="width: 50px; height: 50px; border-radius: 50%;">',
                               obj.photo.url)
        return None

    avatar.short_description = 'Avatar'

    def whatsapp(self, obj):
        if obj.whatsApp:
            return format_html('<a href="https://wa.me/{0}">{0}</a>', obj.whatsApp)
        return None

    def mail(self, obj):
        if obj.email:
            return format_html('<a href="mailto:{0}">{0}</a>', obj.email)
        return None

    def tel(self, obj):
        if obj.phone:
            return format_html('<a href="tel:{0}">{0}</a>', obj.phone)
        return None

    def addresse(self, obj):
        return f'{obj.address} {obj.country}' if obj.address else None


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'order',)
    list_editable = ["name", 'order']
    list_display_links = None


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'isDefault',)
    list_editable = ["isDefault", ]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_editable = ["name", ]
    list_display_links = None
