# Generated by Django 2.2.5 on 2019-09-23 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redapp', '0003_remove_userprofileinfo_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio_site',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='profile_pics',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='destination',
            field=models.CharField(default='ekm', max_length=128),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='location',
            field=models.CharField(default='tvm', max_length=128),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='phone',
            field=models.CharField(default='+91000000', max_length=128),
        ),
    ]
