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
                ('square_url', models.URLField(default=b'http://img3.wikia.nocookie.net/__cb20120730015737/leagueoflegends/images/9/95/ChampionSquare.png')),
                ('champion_id', models.IntegerField(unique=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='freeweek',
            name='slot1',
            field=models.ForeignKey(related_name='+', to='lol.Hero'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freeweek',
            name='slot10',
            field=models.ForeignKey(related_name='+', to='lol.Hero'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freeweek',
            name='slot2',
            field=models.ForeignKey(related_name='+', to='lol.Hero'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freeweek',
            name='slot3',
            field=models.ForeignKey(related_name='+', to='lol.Hero'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freeweek',
            name='slot4',
            field=models.ForeignKey(related_name='+', to='lol.Hero'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freeweek',
            name='slot5',
            field=models.ForeignKey(related_name='+', to='lol.Hero'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freeweek',
            name='slot6',
            field=models.ForeignKey(related_name='+', to='lol.Hero'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freeweek',
            name='slot7',
            field=models.ForeignKey(related_name='+', to='lol.Hero'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freeweek',
            name='slot8',
            field=models.ForeignKey(related_name='+', to='lol.Hero'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freeweek',
            name='slot9',
            field=models.ForeignKey(related_name='+', to='lol.Hero'),
            preserve_default=True,
        ),
    ]
