# Generated by Django 2.2.5 on 2019-09-23 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redapp', '0005_auto_20190923_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pics', models.ImageField(blank=True, upload_to='profile_pics')),
            ],
        ),
    ]
