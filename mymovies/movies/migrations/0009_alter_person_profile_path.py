# Generated by Django 4.2.6 on 2023-10-22 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_person_profile_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profile_path',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]