# Generated by Django 2.2 on 2021-02-15 04:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, default='xxx', max_length=50, null=True)),
                ('url', models.CharField(blank=True, default='xxx', max_length=512, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Client Connection',
                'verbose_name_plural': 'Client Connections',
            },
        ),
        migrations.CreateModel(
            name='MovieView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, default='xxx', max_length=50, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('movie_id', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Movie View',
                'verbose_name_plural': 'Movie Views',
            },
        ),
        migrations.CreateModel(
            name='UserClientConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, default='xxx', max_length=50, null=True)),
                ('url', models.CharField(blank=True, default='xxx', max_length=512, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Client Connection',
                'verbose_name_plural': 'User Client Connections',
            },
        ),
    ]
