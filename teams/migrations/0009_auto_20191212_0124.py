# Generated by Django 2.2.6 on 2019-12-11 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0008_auto_20191208_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='teams', to='teams.Tag', verbose_name='태그'),
        ),
    ]
