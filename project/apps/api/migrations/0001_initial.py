# Generated by Django 2.2.7 on 2019-11-19 16:37

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LastRequestReposGithubApi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(default=True)),
                ('githubApiUrls', django.contrib.postgres.fields.jsonb.JSONField(default='[]')),
                ('lastTenReposSent', django.contrib.postgres.fields.jsonb.JSONField(default='[]')),
                ('lastRequest', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
