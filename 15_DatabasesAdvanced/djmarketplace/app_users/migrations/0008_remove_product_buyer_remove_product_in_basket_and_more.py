# Generated by Django 4.0.3 on 2022-03-15 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_users', '0007_product_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='product',
            name='in_basket',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_bought',
        ),
        migrations.CreateModel(
            name='BuyerProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='Название')),
                ('price', models.IntegerField(blank=True, verbose_name='Цена')),
                ('description', models.CharField(default='', max_length=1000, verbose_name='Описание товара')),
                ('is_bought', models.BooleanField(default=False, verbose_name='Куплено')),
                ('in_basket', models.BooleanField(default=False, verbose_name='В корзине')),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer_products', to=settings.AUTH_USER_MODEL, verbose_name='Покупатель')),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer_products', to='app_users.shop', verbose_name='Магазин')),
            ],
            options={
                'verbose_name': 'товары покупателя',
                'verbose_name_plural': 'товары покупателя',
            },
        ),
    ]
