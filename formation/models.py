from django.db import models

from developer.models import Developer


# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    dates = models.CharField(max_length=255)
    salePrice = models.CharField(max_length=255)
    comments = models.TextField(null=True, blank=True)
    # files
    bonOrder = models.FileField(upload_to='projects/', null=True, blank=True)
    invoiceDev = models.FileField(upload_to='projects/', null=True, blank=True)
    invoices = models.ManyToManyField('ProjectInvoice', related_name='projects')

    condition = models.CharField(max_length=255, null=True, default='',
                                 choices=(('distanciel', 'distanciel'), ('presentiel', 'presentiel')))
    # relations
    status = models.ForeignKey('ProjectStatus', on_delete=models.CASCADE, related_name='projects', blank=True,
                               null=True)
    formation = models.ForeignKey('Formation', on_delete=models.CASCADE, blank=True, null=True)
    developers = models.ManyToManyField(Developer, related_name='projects')

    def __str__(self):
        return self.name


class ProjectInvoice(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, verbose_name="Facture")
    file = models.FileField(upload_to='invoices/', null=True, blank=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='invoice')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Facture"
        verbose_name_plural = "Factures"


class ProjectStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, verbose_name="status")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"


class FormationDuration(models.Model):
    id = models.AutoField(primary_key=True)
    duration = models.CharField(max_length=255)

    def __str__(self):
        return self.duration + ' jours'

    class Meta:
        verbose_name = "Durée"
        verbose_name_plural = "Durées"


class FormationSlide(models.Model):
    id = models.AutoField(primary_key=True)
    slide = models.ImageField(upload_to='formations/', null=True, blank=True)
    # relation
    formation = models.ForeignKey('Formation', on_delete=models.CASCADE, related_name='slides')

    class Meta:
        verbose_name = "Slide"
        verbose_name_plural = "Slides"


class Formation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=255, unique=True)
    sourceCode = models.URLField(verbose_name="source code")
    resources = models.URLField(verbose_name="source code")
    process = models.URLField()
    level = models.CharField(max_length=255, null=True, default='', verbose_name="niveau",
                             choices=(
                                 ('initiation', 'initiation'), ('intermédiaire', 'intermédiaire'),
                                 ('avancé', 'avancé')))
    # relation
    duration = models.ForeignKey(FormationDuration, on_delete=models.CASCADE, related_name='formations', blank=True,
                                 null=True)
    sliders = models.ManyToOneRel(FormationSlide, on_delete=models.CASCADE, to='FormationSlide', field_name='formation')
    projects = models.ManyToOneRel('Project', to='Project', field_name='formation',on_delete=models.CASCADE, )

    class Meta:
        verbose_name = "Formation"
        verbose_name_plural = "Formations"


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, help_text="Nom", verbose_name="Nom")
    role = models.CharField(max_length=255, null=False, help_text="Role", verbose_name="Role")
    society = models.CharField(max_length=255, null=False, help_text="société", verbose_name="société")
    phone = models.CharField(max_length=255, null=False, help_text="Téléphone", verbose_name="Téléphone")
    email = models.EmailField(max_length=255, null=False, help_text="Email", verbose_name="Email")
    whatsapp = models.CharField(max_length=255, null=False, help_text="WhatsApp", verbose_name="WhatsApp")
    remarque = models.TextField(max_length=255, null=False, help_text="remarque", verbose_name="remarque")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class Partner(models.Model):
    id = models.AutoField(primary_key=True)
    logo = models.ImageField(upload_to='partners/', null=True, blank=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.contact.name

    class Meta:
        verbose_name = "Partenaire"
        verbose_name_plural = "Partenaires"
