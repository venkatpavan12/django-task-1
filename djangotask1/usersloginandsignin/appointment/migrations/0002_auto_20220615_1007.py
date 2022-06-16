# Generated by Django 3.2.5 on 2022-06-15 04:37

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='time',
        ),
        migrations.AddField(
            model_name='appointment',
            name='etime',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='starttime',
            field=models.TimeField(default=datetime.datetime(2022, 6, 15, 4, 37, 6, 619767, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 6, 15, 4, 37, 6, 619767, tzinfo=utc)),
        ),
    ]
