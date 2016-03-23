# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20160314_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statecapital',
            name='state',
            field=models.OneToOneField(null=True, to='main.State'),
        ),
    ]
