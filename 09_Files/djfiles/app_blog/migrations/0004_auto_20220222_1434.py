# Generated by Django 2.2 on 2022-02-22 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0003_auto_20220221_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=0, upload_to='photos/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]