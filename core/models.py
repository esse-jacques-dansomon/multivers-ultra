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

    def __str__(self):
        return self.name


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, )

    def __str__(self):
        return self.name + " " + self.city + " " + self.street


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Config(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Level(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='skills', blank=True, null=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Developer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    firstName = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    fixTel = models.CharField(max_length=255, blank=True, null=True)
    whatApp = models.CharField(max_length=255, blank=True, null=True)
    otherCanal = models.CharField(max_length=255, blank=True, null=True)
    photo = models.FileField(max_length=255, blank=True, null=True)
    cv = models.FileField(max_length=255, blank=True, null=False, default='')
    linkedin = models.URLField(max_length=255, blank=True, null=True)
    instagram = models.URLField(max_length=255, blank=True, null=True)
    facebook = models.URLField(max_length=255, blank=True, null=True)
    github = models.URLField(max_length=255, blank=True, null=True)
    gitlab = models.URLField(max_length=255, blank=True, null=True)
    bitbucket = models.URLField(max_length=255, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    video = models.FileField(max_length=255, blank=True, null=True)
    tjm = models.CharField(max_length=255, blank=True, null=True)
    annotations = models.TextField(blank=True, null=False)
    availability = models.CharField(max_length=255, blank=True, null=False)
    modeReglement = models.CharField(max_length=255, blank=True, null=False)
    bankAccount = models.CharField(max_length=255, blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, auto_created=True),
    # relations
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='developers', blank=True, null=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='developer')
    skills = models.ManyToManyField(Skill, through='DeveloperSkill', related_name='developer')

    # auth
    def __str__(self):
        return self.name


class DeveloperSkill(models.Model):
    id = models.AutoField(primary_key=True)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='developer_skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='developer_skills')
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='developer_skills')
    experience = models.IntegerField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.developer.name + " " + self.skill.name + " " + self.level.name
