# Generated by Django 3.2.5 on 2022-06-07 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0006_alter_customuser_managers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='emailid',
            new_name='email',
        ),
    ]
