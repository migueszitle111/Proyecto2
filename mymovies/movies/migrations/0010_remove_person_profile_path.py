# Generated by Django 4.2.6 on 2023-10-22 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_alter_person_profile_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='profile_path',
        ),
    ]