# Generated by Django 3.0.8 on 2020-07-20 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='lyrics',
            field=models.TextField(blank=True),
        ),
    ]
