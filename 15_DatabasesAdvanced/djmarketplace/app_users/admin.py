from django.contrib import admin
from .models import Shop, PersonalInfo, Product, BuyerProduct


class ShopAdmin(admin.ModelAdmin):
    list_display = ['label', 'description']
    fields = ['label', 'description']


class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'shop', 'count_product']
    fields = ['title', 'description', 'price', 'shop', 'count_product']
    list_filter = ['shop']


class BuyerProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'shop', 'buyer', 'is_bought']
    fields = ['title', 'description', 'price', 'shop', 'buyer']
    list_filter = ['shop']


admin.site.register(Shop, ShopAdmin)
admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(BuyerProduct, BuyerProductAdmin)