from django.db import models

from address.models import Address
from skill.models import Skill


# Create your models here.
class Level(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,  null=True)
    order = models.IntegerField( null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Niveaux"
        verbose_name = "Niveau"


class Status(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,  null=True)
    isDefault = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Status"
        verbose_name = "Status"


class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,  null=False)
    code = models.CharField(max_length=255,  null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Langues"
        verbose_name = "Langue"


class Developer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,  null=False, help_text="Nom du développeur")
    firstName = models.CharField(max_length=255,  null=False, help_text="Prénom du développeur")
    phone = models.CharField(max_length=255,  null=False, help_text="Téléphone du développeur")
    email = models.EmailField(max_length=255,  null=False, help_text="Email du développeur")
    fixTel = models.CharField(max_length=255,  null=True, help_text="Téléphone fixe du développeur")
    whatsApp = models.CharField(max_length=255,  null=True, help_text="WhatsApp du développeur")
    otherCanal = models.CharField(max_length=255,  null=True, help_text="Autre canal du développeur")
    linkedin = models.URLField(max_length=255,  null=True, help_text="LinkedIn du développeur")
    instagram = models.URLField(max_length=255,  null=True, help_text="Instagram du développeur")
    facebook = models.URLField(max_length=255,  null=True, help_text="Facebook du développeur")
    github = models.URLField(max_length=255,  null=True, help_text="GitHub du développeur")
    gitlab = models.URLField(max_length=255,  null=True, help_text="GitLab du développeur")
    bitbucket = models.URLField(max_length=255,  null=True, help_text="BitBucket du développeur")
    website = models.URLField(max_length=255,  null=True, help_text="Site web du développeur")
    tjm = models.IntegerField( null=True, help_text="TJM du développeur")
    annotations = models.TextField( null=False, help_text="Annotations du développeur")
    availability = models.TextField( null=False, help_text="Disponibilité du développeur")
    modeReglement = models.CharField(max_length=255,  null=False, help_text="Mode de règlement du développeur")
    bankAccount = models.CharField(max_length=255,  null=False, help_text="Compte bancaire du développeur")
    created_at = models.DateTimeField(auto_now_add=True,  null=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True,  null=True, auto_created=True)
    # Files ...
    cv = models.FileField(upload_to='cv/', max_length=255,  null=False, default='', help_text="CV du développeur")
    photo = models.ImageField(upload_to='photos/', max_length=255,  null=False, default='', help_text="Photo du développeur")
    video = models.FileField(upload_to='videos/', max_length=255,  null=True, default='', help_text="Video du développeur")
    # relations
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='developers',  null=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='developer')
    skills = models.ManyToManyField(Skill, through='DeveloperSkill', related_name='developer')
    languages = models.ManyToManyField(Language, related_name='developer')

    # sex : maculin or feminin
    sex = models.CharField(max_length=255,  null=True, default='maculin',
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
        verbose_name_plural = "Competences des developpeurs"
        verbose_name = "Competence du developpeur"
