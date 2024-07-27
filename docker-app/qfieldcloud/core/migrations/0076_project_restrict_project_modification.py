# Generated by Django 3.2.25 on 2024-05-25 10:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0075_auto_20240323_1419"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="has_restricted_projectfiles",
            field=models.BooleanField(
                default=False,
                help_text="Restrict modifications of QGIS/QField projectfiles to managers and administrators.",
            ),
        ),
    ]
