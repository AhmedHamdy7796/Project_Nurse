# Generated by Django 5.0.3 on 2024-04-15 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_basicuser_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicuser',
            name='date_of_birth',
        ),
        migrations.AlterField(
            model_name='basicuser',
            name='addres',
            field=models.CharField(max_length=100),
        ),
    ]