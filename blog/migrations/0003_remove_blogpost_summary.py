# Generated by Django 2.0.2 on 2018-06-18 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180608_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='summary',
        ),
    ]
