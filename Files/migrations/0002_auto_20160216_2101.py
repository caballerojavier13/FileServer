# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuserfolder',
            name='master',
            field=models.IntegerField(null=True, verbose_name=b'\xe4\xb8\x8a\xe7\xba\xa7\xe7\x9b\xae\xe5\xbd\x95'),
        ),
    ]
