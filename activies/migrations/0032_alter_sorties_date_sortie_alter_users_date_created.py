# Generated by Django 4.1.3 on 2022-12-19 23:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activies', '0031_alter_sorties_date_sortie_alter_users_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorties',
            name='date_sortie',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 20, 0, 44, 41, 354923)),
        ),
        migrations.AlterField(
            model_name='users',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 20, 0, 44, 41, 354923)),
        ),
    ]
