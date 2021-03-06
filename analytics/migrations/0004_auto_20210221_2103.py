# Generated by Django 2.2 on 2021-02-22 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_auto_20210221_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientconnection',
            name='city',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='clientconnection',
            name='country_code',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='clientconnection',
            name='country_name',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='clientconnection',
            name='latitude',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='clientconnection',
            name='longitude',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='clientconnection',
            name='metro_code',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='clientconnection',
            name='region_code',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='clientconnection',
            name='region_name',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='clientconnection',
            name='zip_code',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='movieview',
            name='media_type',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='movieview',
            name='movie_id',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='userclientconnection',
            name='city',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='userclientconnection',
            name='country_code',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='userclientconnection',
            name='country_name',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='userclientconnection',
            name='latitude',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='userclientconnection',
            name='longitude',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='userclientconnection',
            name='metro_code',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='userclientconnection',
            name='region_code',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='userclientconnection',
            name='region_name',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='userclientconnection',
            name='zip_code',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
