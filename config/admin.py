from django.contrib import admin
from django.contrib.auth.hashers import make_password

from config.models import Config, User


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'value',)
    list_editable = ["value", ]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')
    readonly_fields = ('username', 'last_login', 'date_joined')

    fieldsets = (
        ('User', {
            'fields': (
            'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'groups',
            'user_permissions',
            'role'
            )
        }),

        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    actions = ['reset_password']

    def reset_password(self, request, queryset):
        queryset.update(password=make_password('123456'))

    reset_password.short_description = 'Reset Password'

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        return readonly_fields + ('username',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(is_superuser=True)
        return qs

    def delete_model(self, request, obj):
        obj.delete()
