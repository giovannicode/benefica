# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_remove_payment_order'),
        ('orders', '0002_auto_20150123_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.OneToOneField(default=1, to='payments.Payment'),
            preserve_default=False,
        ),
    ]
