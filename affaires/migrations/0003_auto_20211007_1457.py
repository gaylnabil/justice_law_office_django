# Generated by Django 2.2.24 on 2021-10-07 14:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adversaires', '0004_auto_20211007_1457'),
        ('clients', '0002_auto_20211007_1457'),
        ('affaires', '0002_auto_20211006_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Departement',
                'verbose_name_plural': 'Departements',
                'db_table': 'departement',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='affaire',
            name='adversaire_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adversaires.Adversaire'),
        ),
        migrations.AddField(
            model_name='affaire',
            name='avocat_adv_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adversaires.AvocatAdversaire'),
        ),
        migrations.AddField(
            model_name='affaire',
            name='charge_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='affaires.AvocatCharge'),
        ),
        migrations.AddField(
            model_name='affaire',
            name='client_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clients.Client'),
        ),
        migrations.AddField(
            model_name='affaire',
            name='complementaire',
            field=models.CharField(choices=[('civil', 'Civil'), ('correctionnel', 'Correctionnel'), ('commercial', 'Commercial'), ('maritime', 'Maritime'), ('administratif', 'Administratif'), ('social', 'social'), ('famille', 'Famille'), ('conseil_juridique', 'Conseil Juridique')], default='standard', max_length=50),
        ),
        migrations.AddField(
            model_name='affaire',
            name='date_dossier',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='affaire',
            name='date_presc',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='affaire',
            name='objet',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='affaire',
            name='reference',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='affaire',
            name='type_affaire',
            field=models.CharField(choices=[('civil', 'Civil'), ('correctionnel', 'Correctionnel'), ('commercial', 'Commercial'), ('maritime', 'Maritime'), ('administratif', 'Administratif'), ('social', 'social'), ('famille', 'Famille'), ('conseil_juridique', 'Conseil Juridique')], default='civil', max_length=50),
        ),
        migrations.AlterField(
            model_name='avocatcharge',
            name='slug',
            field=models.SlugField(blank=True, max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='affaire',
            name='department_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='affaires.Departement'),
        ),
    ]
