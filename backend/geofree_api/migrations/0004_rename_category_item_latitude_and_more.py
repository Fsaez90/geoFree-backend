# Generated by Django 4.1 on 2023-03-05 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geofree_api', '0003_item_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='category',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='dimensions',
            new_name='longitude',
        ),
        migrations.AddField(
            model_name='item',
            name='condition',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
