# Generated by Django 4.2.6 on 2023-10-22 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_person_file_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='file_path',
        ),
    ]