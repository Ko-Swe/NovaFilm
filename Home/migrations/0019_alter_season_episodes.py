# Generated by Django 3.2.9 on 2021-12-14 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0018_auto_20211130_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='Episodes',
            field=models.ManyToManyField(default=None, to='Home.Episode'),
        ),
    ]
