# Generated by Django 4.1 on 2023-03-05 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geofree_api', '0005_alter_item_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
