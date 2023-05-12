from django.contrib import admin
from django_admin_multi_select_filter.filters import MultiSelectFieldListFilter
from djangoql.admin import DjangoQLSearchMixin
from import_export.admin import ImportExportModelAdmin

from developer.models import Developer, DeveloperSkill, Status, Level


# Register your models here.
@admin.register(Developer)
class DeveloperAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'phone', 'address', 'status', 'competences', 'created_at', 'updated_at')
    list_editable = ["status", ]
    # fields = ('tjm', 'annotations', 'status', 'availability', 'modeReglement', 'bankAccount')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = (
        ('status__name', MultiSelectFieldListFilter),
        ('address__country__name', MultiSelectFieldListFilter),
        ('skills__name', MultiSelectFieldListFilter),
        ('skills__category__name', MultiSelectFieldListFilter),
        ('developer_skills__level__name', MultiSelectFieldListFilter),
        'sex',
    )

    def competences(self, obj):
        # transform to str competence with level and experience
        return ', '.join([f'{devSkill}' for devSkill in DeveloperSkill.objects.filter(developer=obj)])


@admin.register(DeveloperSkill)
class DeveloperSkillAdmin(admin.ModelAdmin):
    list_display = ('developer', 'skill', 'level', 'experience')


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', )
    list_editable = ["name", 'order']
    list_display_links = None


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'isDefault',)
    list_editable = ["isDefault", ]