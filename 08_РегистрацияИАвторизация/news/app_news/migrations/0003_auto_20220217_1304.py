# Generated by Django 2.2 on 2022-02-17 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0002_news_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'permissions': (('can_publish', 'Может публиковать'),)},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': (('can_verify', 'Может верифицировать'),)},
        ),
    ]
