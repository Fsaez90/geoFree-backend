# Generated by Django 4.1 on 2023-03-05 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geofree_api', '0009_item_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]