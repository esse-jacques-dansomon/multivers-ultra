from django.db import models

# Create your models here.

from django.db import models


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, verbose_name="pays")
    code = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Pays"
        verbose_name = "Pays"


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Adresse")
    city = models.CharField(max_length=255, verbose_name="Ville")
    street = models.CharField(max_length=255, verbose_name="Rue")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Pays", related_name='addresses',
                                related_query_name='address')

    def __str__(self):
        return self.country.name + " " + self.city + " " + self.street

    class Meta:
        ordering = ['country']
        verbose_name_plural = "Adresses"
        verbose_name = "Adresse"
