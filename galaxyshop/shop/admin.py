from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Category, Product, Brand, CustomUser, CartItem, Cart

from .forms import CustomUserCreationForm, CustomUserChangeForm

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Cart)
admin.site.register(CartItem)
 

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

admin.site.register(CustomUser, CustomUserAdmin)