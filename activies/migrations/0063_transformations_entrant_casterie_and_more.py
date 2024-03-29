# Generated by Django 4.1.3 on 2023-01-19 22:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activies', '0062_alter_users_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='transformations',
            name='entrant_casterie',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='transformations',
            name='entrant_etain',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='transformations',
            name='teneur_casterie',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='transformations',
            name='teneur_etain',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='users',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 19, 23, 32, 52, 697510)),
        ),
    ]
