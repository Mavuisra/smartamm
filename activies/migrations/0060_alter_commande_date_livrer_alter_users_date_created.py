# Generated by Django 4.1.3 on 2023-01-19 22:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activies', '0059_alter_commande_date_commander_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='date_livrer',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 19, 23, 15, 11, 676507)),
        ),
    ]
