# Generated by Django 4.1 on 2022-08-26 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0009_notifications_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='recepient',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Notifications_recepient', to='wallet.account'),
        ),
    ]
