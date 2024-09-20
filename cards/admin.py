from django.contrib import admin
from .models import Category, Item, ItemImages


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(ItemImages)
class ItemImagesAdmin(admin.ModelAdmin):
    pass
