# Generated by Django 2.2.7 on 2019-11-22 14:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturer_app', '0003_auto_20191122_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='m_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 22, 20, 42, 43, 145999)),
        ),
    ]
