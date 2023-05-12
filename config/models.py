# Create your models here.

from django.db import models


class Config(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=False, unique=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Configurations"
        verbose_name = "Configuration"
