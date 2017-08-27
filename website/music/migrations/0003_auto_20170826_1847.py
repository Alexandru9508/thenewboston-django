# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_if_favorite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='if_favorite',
            new_name='is_favorite',
        ),
    ]
