# Generated by Django 3.0.14 on 2023-06-19 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0002_auto_20230606_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
