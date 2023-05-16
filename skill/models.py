from django.db import models


# Create your models here.

class SkillCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True, unique=True, verbose_name="Categorie de competence")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Categories de competences"
        verbose_name = "Categorie de competence"


class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=False, unique=True, verbose_name="compétence")
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Competences"
        verbose_name = "Competence"
