# Generated by Django 2.2 on 2021-02-13 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210212_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='added',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='media_type',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]