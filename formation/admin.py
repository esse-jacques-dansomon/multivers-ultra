from django.contrib import admin

# Register your models here.
from django.contrib.admin import RelatedFieldListFilter
from djangoql.admin import DjangoQLSearchMixin
from import_export.admin import ImportExportModelAdmin

from formation.models import Project, ProjectInvoice, ProjectStatus, FormationDuration, Partner, Contact, Formation


@admin.register(Project)
class ProjectAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
    list_display = ('name', 'status', 'formation', 'condition', 'dates', 'salePrice')
    search_fields = ('name', 'status', 'formation', 'condition', 'dates', 'salePrice')
    ordering = ('name', 'status', 'formation', 'condition', 'dates', 'salePrice')
    filter_horizontal = ('developers', 'invoices')
    # filter_vertical = ('developers', 'invoices')
    list_filter = (
        ('status__name', RelatedFieldListFilter),
        ('formation__name', RelatedFieldListFilter),
        ('d__name', RelatedFieldListFilter),
    )


@admin.register(ProjectInvoice)
class ProjectInvoiceAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
    list_display = ('name', 'file', 'project',)
    search_fields = ('name', 'file', 'project',)


@admin.register(ProjectStatus)
class ProjectStatusAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(FormationDuration)
class FormationDurationAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
    list_display = ('duration',)
    search_fields = ('duration',)


class PartnerContactInline(admin.TabularInline):
    model = Contact
    extra = 1


@admin.register(Partner)
class PartnerAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
    list_display = ('logo', )
    search_fields = ('logo', )


@admin.register(Formation)
class FormationAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
    list_display = ('name', 'code', 'sourceCode', 'level', 'duration')
    search_fields = ('name', 'code', 'sourceCode', 'level', 'duration')
