# Generated by Django 4.1 on 2022-08-26 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0022_account_account_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='balance',
            field=models.IntegerField(default=None),
        ),
    ]
