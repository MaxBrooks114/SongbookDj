# Generated by Django 3.0.8 on 2021-02-17 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_auto_20210216_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='start',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
