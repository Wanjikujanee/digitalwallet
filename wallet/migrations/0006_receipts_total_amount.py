# Generated by Django 4.1 on 2022-08-26 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_loan_loan_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipts',
            name='total_amount',
            field=models.IntegerField(default=None),
        ),
    ]
