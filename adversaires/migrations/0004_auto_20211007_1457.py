# Generated by Django 2.2.24 on 2021-10-07 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adversaires', '0003_auto_20210930_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adversaire',
            name='observation',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='avocatadversaire',
            name='observation',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
    ]
