from django.contrib import admin
from .models import Item, BannerImg, ContactModel

admin.site.register(Item)
admin.site.register(ContactModel)
admin.site.register(BannerImg)
