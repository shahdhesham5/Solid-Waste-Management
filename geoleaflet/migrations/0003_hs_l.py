# Generated by Django 2.2.16 on 2021-02-23 13:10

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geoleaflet', '0002_hs'),
    ]

    operations = [
        migrations.AddField(
            model_name='hs',
            name='l',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]
