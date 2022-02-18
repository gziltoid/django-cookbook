from django.contrib import admin
from .models import Product, RecipeIngredient, Recipe, Unit


admin.site.register(RecipeIngredient)
admin.site.register(Recipe)
admin.site.register(Product)
admin.site.register(Unit)



