# Generated by Django 4.1.3 on 2022-12-21 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0004_rename_image_realtor_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y-%m-%d'),
        ),
    ]
