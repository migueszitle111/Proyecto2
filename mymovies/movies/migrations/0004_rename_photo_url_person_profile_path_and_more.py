# Generated by Django 4.2.6 on 2023-10-22 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_rename_biography_person_overview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='photo_url',
            new_name='profile_path',
        ),
        migrations.RemoveField(
            model_name='person',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='person',
            name='birthplace',
        ),
        migrations.RemoveField(
            model_name='person',
            name='overview',
        ),
    ]