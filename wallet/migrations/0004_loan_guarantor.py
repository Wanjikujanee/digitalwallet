# Generated by Django 4.1 on 2022-08-26 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_reward_customer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='guarantor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Loan_guarantor', to='wallet.customer'),
        ),
    ]
