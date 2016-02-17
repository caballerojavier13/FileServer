# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Files', '0004_auto_20160216_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='torifile',
            name='folder',
            field=models.TextField(null=True, verbose_name=b'\xe6\x94\xbe\xe7\xbd\xae\xe7\x9b\xae\xe5\xbd\x95'),
        ),
    ]
