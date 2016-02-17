# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Files', '0003_torifile_upload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='torifile',
            old_name='fname',
            new_name='name',
        ),
    ]
