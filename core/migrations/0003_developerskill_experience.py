# Generated by Django 4.2.1 on 2023-05-10 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_developer_skills"),
    ]

    operations = [
        migrations.AddField(
            model_name="developerskill",
            name="experience",
            field=models.IntegerField(blank=True, max_length=255, null=True),
        ),
    ]