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
            name='bust_url',
            field=models.URLField(default=b'http://www.chinatechnews.com/wp-content/uploads/lol-of-the-storm-logo.jpg'),
            preserve_default=True,
        ),
    ]
