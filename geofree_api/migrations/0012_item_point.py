# Generated by Django 4.1.7 on 2023-03-19 12:08

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geofree_api', '0011_remove_item_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]
