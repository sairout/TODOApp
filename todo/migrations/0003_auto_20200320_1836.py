# Generated by Django 3.0.4 on 2020-03-20 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200320_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='time_added',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='username',
        ),
    ]
