# Generated by Django 3.2.5 on 2022-06-15 11:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_auto_20220615_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 6, 15, 11, 53, 29, 497777, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='starttime',
            field=models.TimeField(default=datetime.datetime(2022, 6, 15, 11, 53, 29, 497777, tzinfo=utc)),
        ),
    ]
