# Generated by Django 3.0.4 on 2020-03-23 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20200320_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='user_id',
            field=models.EmailField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
