# Generated by Django 2.2.24 on 2021-10-12 12:08

from django.db import migrations, models
import django.utils.timezone
import parents.parent


class Migration(migrations.Migration):

    dependencies = [
        ('affaires', '0005_auto_20211012_1206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='affaire',
            options={'managed': True, 'ordering': ('-created_at',), 'verbose_name': 'Affaire', 'verbose_name_plural': 'Affaires'},
        ),
        migrations.AlterModelOptions(
            name='avocatcharge',
            options={'managed': True, 'ordering': ('-created_at',), 'verbose_name': 'AvocatCharge', 'verbose_name_plural': 'AvocatCharges'},
        ),
        migrations.AlterModelOptions(
            name='departement',
            options={'managed': True, 'ordering': ('-created_at',), 'verbose_name': 'Departement', 'verbose_name_plural': 'Departements'},
        ),
        migrations.AddField(
            model_name='affaire',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de création'),
        ),
        migrations.AddField(
            model_name='affaire',
            name='updated_at',
            field=parents.parent.AutoDateTimeField(default=django.utils.timezone.now, verbose_name='Date de modification'),
        ),
        migrations.AddField(
            model_name='departement',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de création'),
        ),
        migrations.AddField(
            model_name='departement',
            name='updated_at',
            field=parents.parent.AutoDateTimeField(default=django.utils.timezone.now, verbose_name='Date de modification'),
        ),
    ]
