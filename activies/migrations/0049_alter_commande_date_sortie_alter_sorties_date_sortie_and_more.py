# Generated by Django 4.1.3 on 2023-01-12 08:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activies', '0048_entrees_prix_total_alter_commande_date_sortie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='date_sortie',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 9, 54, 2, 925534)),
        ),
        migrations.AlterField(
            model_name='sorties',
            name='date_sortie',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 9, 54, 2, 925534)),
        ),
        migrations.AlterField(
            model_name='users',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 9, 54, 2, 925534)),
        ),
    ]
