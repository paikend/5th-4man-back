# Generated by Django 2.2.6 on 2019-12-31 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0010_auto_20191212_0124'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Application',
        ),
        migrations.DeleteModel(
            name='Recruit',
        ),
    ]