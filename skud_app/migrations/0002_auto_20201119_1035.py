# Generated by Django 3.1.3 on 2020-11-19 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skud_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userLevels',
            field=models.ManyToManyField(blank=True, to='skud_app.Level'),
        ),
    ]
