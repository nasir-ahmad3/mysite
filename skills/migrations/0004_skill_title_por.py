# Generated by Django 4.1 on 2022-12-17 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_remove_skill_learn_presentage_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='title_por',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
