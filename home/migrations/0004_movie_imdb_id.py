# Generated by Django 2.2 on 2021-02-14 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210213_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='imdb_id',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
