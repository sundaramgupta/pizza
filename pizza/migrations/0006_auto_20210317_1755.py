# Generated by Django 2.2.5 on 2021-03-17 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0005_auto_20210317_1735'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='Order',
        ),
    ]