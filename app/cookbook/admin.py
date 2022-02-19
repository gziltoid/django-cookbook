from django.contrib import admin
from cookbook.models import Product, Ingredient, Recipe, Unit
from django.contrib.auth.models import User, Group

admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ['name']


class IngredientInline(admin.TabularInline):
    list_display = ('product', 'quantity', 'unit',)
    model = Ingredient
    extra = 3


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    inlines = [IngredientInline]
    search_fields = ['title']
    ordering = ('title',)
