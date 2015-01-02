# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FreeWeek',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateField()),
                ('end', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('bust_url', models.URLField(default=b'http://www.chinatechnews.com/wp-content/uploads/lol-of-the-storm-logo.jpg')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='freeweek',
            name='slot1',
            field=models.ForeignKey(related_name='+', to='heroes.Hero'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freeweek',
            name='slot2',
            field=models.ForeignKey(related_name='+', to='heroes.Hero'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freeweek',
            name='slot3',
            field=models.ForeignKey(related_name='+', to='heroes.Hero'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freeweek',
            name='slot4',
            field=models.ForeignKey(related_name='+', to='heroes.Hero'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freeweek',
            name='slot5',
            field=models.ForeignKey(related_name='+', to='heroes.Hero'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freeweek',
            name='slot6',
            field=models.ForeignKey(related_name='+', to='heroes.Hero'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freeweek',
            name='slot7',
            field=models.ForeignKey(related_name='+', to='heroes.Hero'),
            preserve_default=True,
        ),
    ]
