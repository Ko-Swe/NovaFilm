# Generated by Django 3.2 on 2021-11-27 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_episode_season_serial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='episode_number',
            field=models.CharField(default='E01 - Serial Name', max_length=50),
        ),
        migrations.AlterField(
            model_name='season',
            name='season_name',
            field=models.CharField(default='S01 - Serial Name', max_length=50),
        ),
    ]
