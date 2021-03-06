# Generated by Django 2.2.7 on 2019-11-22 12:43

import datetime
from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_name', models.CharField(help_text='manufacturer company name', max_length=100)),
                ('m_phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('m_address', models.TextField(blank=True, null=True)),
                ('m_details', models.TextField(blank=True, null=True)),
                ('m_previous_blance', models.DecimalField(decimal_places=2, max_digits=12)),
                ('m_date', models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 22, 18, 43, 12, 812835))),
            ],
        ),
    ]
