# Generated by Django 4.1 on 2022-08-26 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0018_transaction_transaction_charge'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_amount',
            field=models.IntegerField(default=None),
        ),
    ]
