# Generated by Django 2.2.24 on 2021-10-07 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('affaires', '0003_auto_20211007_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departement',
            old_name='nom',
            new_name='nom_depart',
        ),
    ]
