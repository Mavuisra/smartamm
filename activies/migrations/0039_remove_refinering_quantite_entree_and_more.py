# Generated by Django 4.1.3 on 2023-11-28 16:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activies', '0038_alter_entrees_teneur_alter_sorties_date_sortie_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refinering',
            name='quantite_entree',
        ),
        migrations.AlterField(
            model_name='sorties',
            name='date_sortie',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 17, 50, 38, 11220)),
        ),
        migrations.AlterField(
            model_name='users',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 17, 50, 38, 11220)),
        ),
    ]
