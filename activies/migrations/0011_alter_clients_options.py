# Generated by Django 4.1.3 on 2022-12-05 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activies', '0010_delete_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clients',
            options={'ordering': ['created_at']},
        ),
    ]
