# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-25 19:08
from __future__ import unicode_literals

import annoying.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_markdown.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', django_markdown.models.MarkdownField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'date published')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'date updated')),
                ('answer', models.BooleanField(default=False)),
                ('positive_votes', models.IntegerField(default=0)),
                ('negative_votes', models.IntegerField(default=0)),
                ('total_points', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-answer', '-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='AnswerComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'date published')),
                ('comment_text', django_markdown.models.MarkdownField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnswerVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', django_markdown.models.MarkdownField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'date published')),
                ('reward', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('closed', models.BooleanField(default=False)),
                ('positive_votes', models.IntegerField(default=0)),
                ('negative_votes', models.IntegerField(default=0)),
                ('total_points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'date published')),
                ('comment_text', models.CharField(max_length=250)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.Question')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BooleanField(default=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.Question')),
            ],
        ),
        migrations.CreateModel(
            name='UserQAProfile',
            fields=[
                ('user', annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('points', models.IntegerField(default=0)),
                ('website', models.URLField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='questionvote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='questioncomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]