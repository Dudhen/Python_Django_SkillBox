# Generated by Django 2.2 on 2022-03-03 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_shop', '0005_auto_20220303_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='buyer_id',
        ),
        migrations.AddField(
            model_name='offer',
            name='buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offers', to=settings.AUTH_USER_MODEL, verbose_name='Покупатель'),
        ),
    ]
