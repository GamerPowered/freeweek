# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='champion_id',
            field=models.IntegerField(unique=True, null=True),
            preserve_default=True,
        ),
    ]
