# Generated by Django 5.0.3 on 2024-04-24 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.CharField(max_length=100),
        ),
    ]
