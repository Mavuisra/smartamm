# Generated by Django 4.1.3 on 2023-01-20 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activies', '0070_alter_users_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 20, 10, 15, 22, 531193)),
        ),
    ]
