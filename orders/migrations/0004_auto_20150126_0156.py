# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='tile',
            new_name='title',
        ),
    ]
