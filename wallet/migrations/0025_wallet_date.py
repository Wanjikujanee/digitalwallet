# Generated by Django 4.1 on 2022-08-26 06:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0024_wallet_currency_alter_wallet_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]