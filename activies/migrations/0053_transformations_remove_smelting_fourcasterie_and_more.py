# Generated by Django 4.1.3 on 2023-01-19 19:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activies', '0052_commande_prix_total_alter_commande_date_sortie_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='transformations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite_entrer_casterie', models.FloatField(default=0.0)),
                ('quantite_sortie_casterie', models.FloatField(default=0.0)),
                ('quantite_entrer_etain', models.FloatField(default=0.0)),
                ('quantite_sortie_etain', models.FloatField(default=0.0)),
                ('date_entrer', models.DateTimeField(auto_now_add=True)),
                ('date_sortie', models.DateTimeField(auto_now=True)),
                ('fourcasterie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activies.fourcasterie')),
                ('fourrafine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activies.fourrafine')),
                ('produits', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activies.produits')),
            ],
        ),
        migrations.RemoveField(
            model_name='smelting',
            name='fourcasterie',
        ),
        migrations.RemoveField(
            model_name='smelting',
            name='produits',
        ),
        migrations.RemoveField(
            model_name='smelting',
            name='user',
        ),
        migrations.RemoveField(
            model_name='entrees',
            name='date_sortie',
        ),
        migrations.RemoveField(
            model_name='entrees',
            name='tvaPourcentage',
        ),
        migrations.AddField(
            model_name='entrees',
            name='descriptions',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='entrees',
            name='source_minier',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='commande',
            name='date_sortie',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 19, 20, 51, 31, 874007)),
        ),
        migrations.AlterField(
            model_name='depanses',
            name='name',
            field=models.CharField(default='', max_length=222, null=True),
        ),
        migrations.RemoveField(
            model_name='entrees',
            name='depanses',
        ),
        migrations.AlterField(
            model_name='entrees',
            name='prix_achat',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='entrees',
            name='prix_total',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='entrees',
            name='quantite',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='entrees',
            name='teneur',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='entrees',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activies.users'),
        ),
        migrations.AlterField(
            model_name='sorties',
            name='date_sortie',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='sorties',
            name='prix_vente',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='sorties',
            name='quantite',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='sorties',
            name='teneur',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='sorties',
            name='tvaPourcentage',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='sorties',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='activies.users'),
        ),
        migrations.AlterField(
            model_name='users',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 19, 20, 51, 31, 874007)),
        ),
        migrations.DeleteModel(
            name='refinering',
        ),
        migrations.DeleteModel(
            name='smelting',
        ),
        migrations.AddField(
            model_name='transformations',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='activies.users'),
        ),
        migrations.AddField(
            model_name='entrees',
            name='depanses',
            field=models.ManyToManyField(to='activies.depanses'),
        ),
    ]
