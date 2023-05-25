# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class Config(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=False, unique=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Configurations"
        verbose_name = "Configuration"


class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Role(models.TextChoices):
        OTHER = None
        ADMIN = "ADMIN", "Admin"
        DEVELOPER = "DEVELOPER", "Developer"
        PARTNER = "PARTNER", "Partner"

    base_role = Role.DEVELOPER

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class DeveloperManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.DEVELOPER)


class DeveloperProxy(User):
    base_role = User.Role.DEVELOPER

    student = DeveloperManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for developers"
