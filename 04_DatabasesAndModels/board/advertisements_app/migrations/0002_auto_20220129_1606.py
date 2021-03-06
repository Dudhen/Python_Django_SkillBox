# Generated by Django 2.2 on 2022-01-29 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
                ('phone', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='advertisement',
            name='views_count',
            field=models.IntegerField(default=0, verbose_name='количество просмотров'),
        ),
    ]
