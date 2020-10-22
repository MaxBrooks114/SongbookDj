# Generated by Django 3.0.8 on 2020-10-19 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20200921_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='element',
            name='instrument',
        ),
        migrations.AddField(
            model_name='element',
            name='instruments',
            field=models.ManyToManyField(to='api.Instrument'),
        ),
    ]
