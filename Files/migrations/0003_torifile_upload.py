# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Files.models


class Migration(migrations.Migration):

    dependencies = [
        ('Files', '0002_auto_20160216_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='torifile',
            name='upload',
            field=models.FileField(upload_to=Files.models.path_and_rename, null=True, verbose_name=b'\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x96\x87\xe4\xbb\xb6\xe8\xb7\xaf\xe5\xbe\x84'),
        ),
    ]
