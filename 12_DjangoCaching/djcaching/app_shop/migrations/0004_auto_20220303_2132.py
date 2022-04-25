# Generated by Django 2.2 on 2022-03-03 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0003_auto_20220303_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='buyer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='offers', to=settings.AUTH_USER_MODEL, verbose_name='Покупатель'),
        ),
    ]