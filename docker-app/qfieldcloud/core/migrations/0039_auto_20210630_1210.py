# Generated by Django 3.2.4 on 2021-06-30 12:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0038_rename_workplace_useraccount_company"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="applyjob",
            options={
                "verbose_name": "Job: apply",
                "verbose_name_plural": "Jobs: apply",
            },
        ),
        migrations.AlterModelOptions(
            name="exportjob",
            options={
                "verbose_name": "Job: export",
                "verbose_name_plural": "Jobs: export",
            },
        ),
    ]
