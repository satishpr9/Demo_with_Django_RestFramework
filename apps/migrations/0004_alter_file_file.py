# Generated by Django 4.0.4 on 2022-05-19 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_file_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.ImageField(blank=True, upload_to='my_pictures'),
        ),
    ]
