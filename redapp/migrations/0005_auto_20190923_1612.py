# Generated by Django 2.2.5 on 2019-09-23 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redapp', '0004_auto_20190923_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='destination',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='location',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='phone',
            field=models.CharField(max_length=128),
        ),
    ]
