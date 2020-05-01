# Generated by Django 2.2 on 2020-05-01 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200430_1651'),
        ('clinic', '0003_auto_20200501_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Patient')),
            ],
        ),
    ]