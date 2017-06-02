# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siad', '0008_auto_20170426_0006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aspirante',
            options={'ordering': ['apellidoPaterno']},
        ),
    ]
