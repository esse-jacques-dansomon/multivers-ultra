# Generated by Django 4.2.1 on 2023-05-17 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Config",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(blank=True, max_length=255, unique=True)),
                ("value", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "verbose_name": "Configuration",
                "verbose_name_plural": "Configurations",
            },
        ),
    ]