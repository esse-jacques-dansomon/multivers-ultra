from django.apps import AppConfig


class DeveloperAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "developer"
    verbose_name = "Développeurs"
