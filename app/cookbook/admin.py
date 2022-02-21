from django.contrib import admin
from cookbook.models import Product, Ingredient, Recipe
from django.contrib.auth.models import User, Group

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.site_header = "Cookbook administration"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ['name__icontains']


class IngredientInline(admin.TabularInline):
    list_display = ('product', 'quantity', 'unit',)
    model = Ingredient
    extra = 3


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_per_page = 25
    inlines = [IngredientInline]
    search_fields = ("title__icontains", "ingredients__product__name__icontains",)
    ordering = ('title',)
