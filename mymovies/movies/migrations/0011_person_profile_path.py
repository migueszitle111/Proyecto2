# Generated by Django 4.2.6 on 2023-10-22 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_remove_person_profile_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='profile_path',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]