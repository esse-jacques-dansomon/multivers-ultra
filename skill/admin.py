from django.contrib import admin

from skill.models import SkillCategory, Skill


# Register your models here.

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_editable = ["name", ]
    list_display_links = None


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_editable = ["name",  "category"]
    list_display_links = None