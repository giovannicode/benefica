# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customusers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_handle',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
    ]
