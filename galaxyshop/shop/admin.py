from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Category, Product, Brand, CartItem, Cart, SubCategory, Hit, Order,Product_images,ProductDescription,Description_info,Recomendations




class ProductDescriptionInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = ProductDescription

@admin.register(Product)
class Product(admin.ModelAdmin):
    
    inlines = [ProductDescriptionInline]

class Description_infoInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Description_info

@admin.register(ProductDescription)
class ProductDescription(admin.ModelAdmin):
    
    inlines = [Description_infoInline]

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(SubCategory)
admin.site.register(Hit)
admin.site.register(Recomendations)
admin.site.register(Order) 
admin.site.register(Product_images)
admin.site.register(Description_info)

