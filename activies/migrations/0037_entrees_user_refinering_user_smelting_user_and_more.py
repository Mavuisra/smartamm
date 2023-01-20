# Generated by Django 4.1.3 on 2023-11-28 02:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activies', '0036_alter_sorties_date_sortie_alter_sorties_prix_total_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrees',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='activies.users'),
        ),
        migrations.AddField(
            model_name='refinering',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='activies.users'),
        ),
        migrations.AddField(
            model_name='smelting',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='activies.users'),
        ),
        migrations.AlterField(
            model_name='sorties',
            name='date_sortie',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 3, 40, 7, 74730)),
        ),
        migrations.AlterField(
            model_name='users',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 3, 40, 7, 74730)),
        ),
    ]
