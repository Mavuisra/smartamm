# Generated by Django 4.1.3 on 2023-01-11 21:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activies', '0046_remove_commande_prix_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='date_sortie',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 11, 22, 18, 57, 262870)),
        ),
        migrations.AlterField(
            model_name='commande',
            name='prix_vente',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sorties',
            name='date_sortie',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 11, 22, 18, 57, 267867)),
        ),
        migrations.AlterField(
            model_name='users',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 11, 22, 18, 57, 267867)),
        ),
    ]
