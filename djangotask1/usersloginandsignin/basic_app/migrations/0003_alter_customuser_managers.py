# Generated by Django 3.2.5 on 2022-06-07 04:17

import basic_app.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_alter_customuser_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', basic_app.models.UserManager()),
            ],
        ),
    ]
