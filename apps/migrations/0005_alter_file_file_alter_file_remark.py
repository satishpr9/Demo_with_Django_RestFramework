# Generated by Django 4.0.4 on 2022-05-19 08:06

import apps.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_alter_file_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.ImageField(blank=True, upload_to=apps.models.file.nameFile),
        ),
        migrations.AlterField(
            model_name='file',
            name='remark',
            field=models.CharField(blank=True, default='satish', max_length=20),
        ),
    ]