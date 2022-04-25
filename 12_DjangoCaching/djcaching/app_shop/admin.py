from django.contrib import admin
from .models import Shop, PersonalInfo, Promotion, Offer


class ShopAdmin(admin.ModelAdmin):
    list_display = ['label', 'description']
    fields = ['label', 'description']


class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance']


class PromotionAdmin(admin.ModelAdmin):
    list_display = ['shop', 'title', 'description']
    fields = ['title', 'description', 'shop']
    list_filter = ['shop']


class OfferAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'shop', 'buyer']
    fields = ['title', 'description', 'price', 'shop']
    list_filter = ['shop']


admin.site.register(Shop, ShopAdmin)
admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(Promotion, PromotionAdmin)
admin.site.register(Offer, OfferAdmin)