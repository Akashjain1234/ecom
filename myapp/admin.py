from django.contrib import admin
from .models import  *
# Register your models here.


@admin.register(MainCategoryModel)
class MainCategoryModelAdmin(admin.ModelAdmin):
    list_display = ["id","info", "image", "name"]


@admin.register(SubCategoryModel)
class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = ["id","info", "image", "name"]


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["status","info", "sell_price", "discounted_price", "discount", "og_price", "image", "name", "scate", "mcate"]


@admin.register(CartModel)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ["quantity", "product", "user","id"]


@admin.register(AddressModel)
class AddressModelAdmin(admin.ModelAdmin):
    list_display = ["id","first_name","last_name","email","address","phone"]


@admin.register(Placeorder)
class PlaceorderAdmin(admin.ModelAdmin):
    list_display = ["status", "quantity", "address", "product", "user"][::-1]
