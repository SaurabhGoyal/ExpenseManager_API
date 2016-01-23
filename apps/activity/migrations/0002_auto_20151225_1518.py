# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitycategory',
            name='name',
            field=models.CharField(unique=True, max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='useractivity',
            unique_together=set([('user', 'activity')]),
        ),
    ]
