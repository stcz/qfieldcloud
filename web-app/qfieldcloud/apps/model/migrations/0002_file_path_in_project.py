# Generated by Django 2.2.6 on 2020-01-24 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='path_in_project',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
    ]
