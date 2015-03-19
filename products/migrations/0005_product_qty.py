# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qty',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
