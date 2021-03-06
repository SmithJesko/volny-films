# Generated by Django 2.2 on 2021-02-22 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210214_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='added',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='awards',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb_id',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb_rating',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='movie',
            name='media_type',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_id',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='movie',
            name='plot',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='popularity',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rated',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='movie',
            name='runtime',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='movie',
            name='writer',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
