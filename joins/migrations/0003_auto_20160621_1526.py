# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0002_join_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='name',
            field=models.CharField(default='Your Name?', max_length=20),
        ),
    ]
