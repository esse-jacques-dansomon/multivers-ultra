# Generated by Django 4.2.1 on 2023-05-25 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("developer", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "name",
                    models.CharField(
                        help_text="Nom", max_length=255, verbose_name="Nom"
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        help_text="Role", max_length=255, verbose_name="Role"
                    ),
                ),
                (
                    "society",
                    models.CharField(
                        help_text="société", max_length=255, verbose_name="société"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        help_text="Téléphone", max_length=255, verbose_name="Téléphone"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Email", max_length=255, verbose_name="Email"
                    ),
                ),
                (
                    "whatsapp",
                    models.CharField(
                        help_text="WhatsApp", max_length=255, verbose_name="WhatsApp"
                    ),
                ),
                (
                    "remarque",
                    models.TextField(
                        help_text="remarque", max_length=255, verbose_name="remarque"
                    ),
                ),
            ],
            options={
                "verbose_name": "Contact",
                "verbose_name_plural": "Contacts",
            },
        ),
        migrations.CreateModel(
            name="Formation",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255, unique=True)),
                ("code", models.CharField(max_length=255, unique=True)),
                ("sourceCode", models.URLField(verbose_name="source code")),
                ("resources", models.URLField(verbose_name="source code")),
                ("process", models.URLField()),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("initiation", "initiation"),
                            ("intermédiaire", "intermédiaire"),
                            ("avancé", "avancé"),
                        ],
                        default="",
                        max_length=255,
                        null=True,
                        verbose_name="niveau",
                    ),
                ),
            ],
            options={
                "verbose_name": "Formation",
                "verbose_name_plural": "Formations",
            },
        ),
        migrations.CreateModel(
            name="FormationDuration",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("duration", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Durée",
                "verbose_name_plural": "Durées",
            },
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255, unique=True)),
                ("dates", models.CharField(max_length=255)),
                ("salePrice", models.CharField(max_length=255)),
                ("comments", models.TextField(blank=True, null=True)),
                (
                    "bonOrder",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="projects/bon_commandes/%Y/%m/%d/",
                    ),
                ),
                (
                    "invoiceDev",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="projects/invoices_dev/%Y/%m/%d/",
                    ),
                ),
                (
                    "condition",
                    models.CharField(
                        choices=[
                            ("distanciel", "distanciel"),
                            ("presentiel", "presentiel"),
                        ],
                        default="",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "developers",
                    models.ManyToManyField(
                        related_name="projects", to="developer.developer"
                    ),
                ),
                (
                    "formation",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="formation.formation",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProjectStatus",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "name",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="status"
                    ),
                ),
            ],
            options={
                "verbose_name": "Status",
                "verbose_name_plural": "Status",
            },
        ),
        migrations.CreateModel(
            name="ProjectInvoice",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "name",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Facture"
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        blank=True, null=True, upload_to="invoices/%Y/%m/%d/"
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invoice",
                        to="formation.project",
                    ),
                ),
            ],
            options={
                "verbose_name": "Facture",
                "verbose_name_plural": "Factures",
            },
        ),
        migrations.AddField(
            model_name="project",
            name="invoices",
            field=models.ManyToManyField(
                related_name="projects", to="formation.projectinvoice"
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="status",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="projects",
                to="formation.projectstatus",
            ),
        ),
        migrations.CreateModel(
            name="Partner",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "logo",
                    models.ImageField(
                        blank=True, null=True, upload_to="partners/%Y/%m/%d/"
                    ),
                ),
                (
                    "contact",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="formation.contact",
                    ),
                ),
            ],
            options={
                "verbose_name": "Partenaire",
                "verbose_name_plural": "Partenaires",
            },
        ),
        migrations.CreateModel(
            name="FormationSlide",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "slide",
                    models.ImageField(
                        blank=True, null=True, upload_to="formations/%Y/%m/%d/"
                    ),
                ),
                (
                    "formation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="slides",
                        to="formation.formation",
                    ),
                ),
            ],
            options={
                "verbose_name": "Slide",
                "verbose_name_plural": "Slides",
            },
        ),
        migrations.AddField(
            model_name="formation",
            name="duration",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="formations",
                to="formation.formationduration",
            ),
        ),
    ]