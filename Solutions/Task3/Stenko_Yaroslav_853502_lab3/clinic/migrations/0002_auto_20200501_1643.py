# Generated by Django 2.2 on 2020-05-01 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.DateField(unique=True),
        ),
    ]
