# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-25 19:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0001_initial'),
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answervote',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.Answer'),
        ),
        migrations.AddField(
            model_name='answervote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answercomment',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.Answer'),
        ),
        migrations.AddField(
            model_name='answercomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='questionvote',
            unique_together=set([('user', 'question')]),
        ),
        migrations.AlterUniqueTogether(
            name='answervote',
            unique_together=set([('user', 'answer')]),
        ),
    ]
