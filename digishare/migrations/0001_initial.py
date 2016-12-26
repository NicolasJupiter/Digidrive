# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-25 19:10
from __future__ import unicode_literals

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
            name='_video',
            fields=[
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('video_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_email', models.CharField(blank=True, max_length=50, null=True)),
                ('video_path', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Site_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('su_student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]