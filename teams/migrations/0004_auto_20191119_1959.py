# Generated by Django 2.2.6 on 2019-11-19 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_team_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(default='default.png', upload_to='team/image/%Y/%m/%d/', verbose_name='이미지'),
        ),
    ]