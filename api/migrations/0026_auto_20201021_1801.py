# Generated by Django 3.0.8 on 2020-10-21 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20201019_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='instruments',
            field=models.ManyToManyField(related_name='elements', to='api.Instrument'),
        ),
    ]
