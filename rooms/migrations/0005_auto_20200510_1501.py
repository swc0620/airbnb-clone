# Generated by Django 2.2.12 on 2020-05-10 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20200510_1414'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='chekc_out',
            new_name='check_out',
        ),
    ]
