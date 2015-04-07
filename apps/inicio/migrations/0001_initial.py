# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=300)),
                ('apellp', models.CharField(max_length=50)),
                ('apellm', models.CharField(max_length=50)),
                ('edad', models.IntegerField(default=0)),
                ('carrera', models.CharField(max_length=100)),
            ],
        ),
    ]
