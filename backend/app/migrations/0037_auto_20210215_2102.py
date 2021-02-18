# Generated by Django 3.0.8 on 2021-02-15 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_auto_20210202_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='acousticness',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='danceability',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='energy',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='instrumentalness',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='liveness',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='loudness',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='speechiness',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='tempo',
            field=models.FloatField(blank=True, default=60, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='time_signature',
            field=models.IntegerField(blank=True, default=4, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='valence',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='year',
            field=models.CharField(blank=True, default=2021, max_length=200),
        ),
    ]
