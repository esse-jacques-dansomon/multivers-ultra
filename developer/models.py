from django.db import models

from address.models import Address
from skill.models import Skill


# Create your models here.
class Level(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,  blank=True,null=True, unique=True, verbose_name="niveau")
    order = models.IntegerField(blank=True,null=True, unique=True, verbose_name="ordre")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Niveaux"
        verbose_name = "Niveau"


class Status(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,  blank=True,null=True, unique=True, verbose_name="statut")
    isDefault = models.BooleanField(default=False, verbose_name="par défaut")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Status"
        verbose_name = "Status"


class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,  null=False, unique=True, verbose_name="langue")
    code = models.CharField(max_length=255,  null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Langues"
        verbose_name = "Langue"


class Developer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, help_text="Nom du développeur", verbose_name="Nom")
    firstName = models.CharField(max_length=255,  null=False, help_text="Prénom du développeur", verbose_name="Prénom")
    phone = models.CharField(max_length=255,  null=False, help_text="Téléphone du développeur", verbose_name="Téléphone")
    email = models.EmailField(max_length=255,  null=False, help_text="Email du développeur", verbose_name="Email")
    fixTel = models.CharField(max_length=255,  blank=True,null=True, help_text="Téléphone fixe du développeur", verbose_name="Téléphone fixe")
    whatsApp = models.CharField(max_length=255,  blank=True,null=True, help_text="WhatsApp du développeur", verbose_name="WhatsApp")
    otherCanal = models.CharField(max_length=255,  blank=True,null=True, help_text="Autre canal du développeur", verbose_name="Autre canal")
    linkedin = models.URLField(max_length=255,  blank=True,null=True, help_text="LinkedIn du développeur", verbose_name="LinkedIn")
    instagram = models.URLField(max_length=255,  blank=True,null=True, help_text="Instagram du développeur")
    facebook = models.URLField(max_length=255,  blank=True,null=True, help_text="Facebook du développeur")
    github = models.URLField(max_length=255,  blank=True,null=True, help_text="GitHub du développeur")
    gitlab = models.URLField(max_length=255,  blank=True,null=True, help_text="GitLab du développeur")
    bitbucket = models.URLField(max_length=255,  blank=True,null=True, help_text="BitBucket du développeur")
    website = models.URLField(max_length=255,  blank=True,null=True, help_text="Site web du développeur", verbose_name="Site web")
    tjm = models.IntegerField( blank=True,null=True, help_text="TJM du développeur")
    annotations = models.TextField( null=False, help_text="Annotations du développeur")
    availability = models.TextField( null=False, help_text="Disponibilité du développeur", verbose_name="Disponibilité")
    modeReglement = models.CharField(max_length=255,  null=False, help_text="Mode de règlement du développeur")
    bankAccount = models.CharField(max_length=255,  null=False, help_text="Compte bancaire du développeur")
    created_at = models.DateTimeField(auto_now_add=True,  blank=True,null=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True,  blank=True,null=True, auto_created=True)
    # Files ...
    cv = models.FileField(upload_to='cv/', max_length=255,  null=False, default='', help_text="CV du développeur")
    photo = models.ImageField(upload_to='photos/', max_length=255,  null=False, default='', help_text="Photo du développeur")
    video = models.FileField(upload_to='videos/', max_length=255,  blank=True,null=True, default='', help_text="Video du développeur")
    # relations
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='developers',  null=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='developer')
    skills = models.ManyToManyField(Skill, through='DeveloperSkill', related_name='developer')
    languages = models.ManyToManyField(Language, related_name='developer')

    # sex : maculin or feminin
    sex = models.CharField(max_length=255,  null=False, default='maculin',
                           choices=(('maculin', 'maculin'), ('feminin', 'feminin')))

    # auth
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Developpeurs"
        verbose_name = "Developpeur"


class DeveloperSkill(models.Model):
    id = models.AutoField(primary_key=True)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='developer_skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='developer_skills')
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='developer_skills')
    experience = models.IntegerField( null=True)

    def __str__(self):
        return self.skill.name + " : " + self.level.name

    class Meta:
        verbose_name_plural = "Competences du developpeur"
        verbose_name = "Competence du developpeur"
