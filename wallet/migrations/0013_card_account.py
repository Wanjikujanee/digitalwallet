# Generated by Django 4.1 on 2022-08-26 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0012_thirdparty_id_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='account',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Card_account', to='wallet.account'),
        ),
    ]
