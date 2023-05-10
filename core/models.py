# Create your models here.
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.forms import MultipleChoiceField, ChoiceField

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, )


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)


class Config(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)


class Level(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)


class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='skills', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='skills', blank=True, null=True)


class Status(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)


class Developer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    firstName = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    fixTel = models.CharField(max_length=255, blank=True, null=True)
    whatApp = models.CharField(max_length=255, blank=True, null=True)
    otherCanal = models.CharField(max_length=255, blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    cv = models.CharField(max_length=255, blank=True, null=False, default='')
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    github = models.CharField(max_length=255, blank=True, null=True)
    gitlab = models.CharField(max_length=255, blank=True, null=True)
    bitbucket = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    video = models.CharField(max_length=255, blank=True, null=True)
    tjm = models.CharField(max_length=255, blank=True, null=True)
    annotations = models.CharField(max_length=255, blank=True, null=False)
    availability = models.CharField(max_length=255, blank=True, null=False)
    modeReglement = models.CharField(max_length=255, blank=True, null=False)
    bankAccount = models.CharField(max_length=255, blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True),
    # relations
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='developers', blank=True, null=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='developer')
    skills = models.ManyToManyField(Skill, related_name='developers', blank=True)
    # auth
