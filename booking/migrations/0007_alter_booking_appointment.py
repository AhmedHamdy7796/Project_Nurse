# Generated by Django 5.0.3 on 2024-04-18 02:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_alter_booking_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='appointment',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 18, 9, 0)),
        ),
    ]