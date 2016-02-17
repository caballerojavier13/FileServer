# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TOriFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.IntegerField(default=0, verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe6\x95\xb0\xe9\x87\x8f')),
                ('md5', models.CharField(max_length=40, verbose_name=b'MD5')),
                ('path', models.TextField(verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6\xe8\xb7\xaf\xe5\xbe\x84')),
                ('fname', models.TextField(verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6\xe5\x90\x8d')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4', null=True)),
                ('mimetype', models.CharField(max_length=40, null=True, verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6\xe7\xb1\xbb\xe5\x9e\x8b')),
            ],
        ),
        migrations.CreateModel(
            name='TUserFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6\xe5\x90\x8d')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
        migrations.CreateModel(
            name='TUserFolder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('master', models.IntegerField(default=0, verbose_name=b'\xe4\xb8\x8a\xe7\xba\xa7\xe7\x9b\xae\xe5\xbd\x95')),
                ('name', models.TextField(verbose_name=b'\xe7\x9b\xae\xe5\xbd\x95\xe5\x90\x8d')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tuserfile',
            name='master',
            field=models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\x9c\xa8\xe7\x9b\xae\xe5\xbd\x95', to='Files.TUserFolder'),
        ),
        migrations.AddField(
            model_name='tuserfile',
            name='ori',
            field=models.ForeignKey(verbose_name=b'\xe5\x8e\x9f\xe6\x96\x87\xe4\xbb\xb6', to='Files.TOriFile'),
        ),
        migrations.AddField(
            model_name='tuserfile',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL),
        ),
    ]
