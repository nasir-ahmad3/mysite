# Generated by Django 4.1 on 2022-12-24 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_delete_djangoprojects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='Project',
        ),
        migrations.AddField(
            model_name='project',
            name='downlaod_link',
            field=models.URLField(null=True),
        ),
    ]
