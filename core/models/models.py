# Create your models here.
from django.db import models
from django.forms import MultipleChoiceField, ChoiceField

# Create your models here.


class Kind(models.Model):
    name = models.CharField(max_length=1)

    def __str__(self):
        return self.name


class Languages(models.Model):
    name = models.CharField(max_length=4)

    def __str__(self):
        return self.name


class Niveau(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=4)

    def __str__(self):
        return self.name


class Developer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    firstname = models.CharField(max_length=100 , null=True)
    name = models.CharField(max_length=100 , null=True)
    phone = models.CharField(max_length=100, null=True)
    whatApps = models.CharField(max_length=100, null=True)
    age = models.IntegerField()
    kind = models.ForeignKey(null=True, on_delete=models.CASCADE, blank=True, to="kind")
    address = models.TextField(max_length=400)
    country = models.CharField(max_length=150)
    mail = models.EmailField()
    languages = models.ManyToManyField(blank=True, to="languages")
    github = models.CharField(max_length=130)
    linkedin = models.CharField(max_length=140)
    photo = models.FileField(help_text="Photo de profile", null=True, blank=True)
    cv = models.FileField(help_text="CV en pdf", null=True, blank=True)
    site = models.CharField(max_length=140, null=True, blank=True)
    page = models.CharField(max_length=140)
    objects = models.Manager()