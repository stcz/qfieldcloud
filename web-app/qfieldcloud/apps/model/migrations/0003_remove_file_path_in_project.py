# Generated by Django 2.2.6 on 2020-01-24 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_file_path_in_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='path_in_project',
        ),
    ]
