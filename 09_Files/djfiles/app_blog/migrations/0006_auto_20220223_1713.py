# Generated by Django 2.2 on 2022-02-23 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0005_auto_20220222_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ImageField(default=0, upload_to='photos/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
