# Generated by Django 4.1 on 2022-12-21 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_djangoprojects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_id',
        ),
        migrations.AddField(
            model_name='djangoprojects',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
    ]