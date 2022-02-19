from django.shortcuts import render, get_object_or_404, get_list_or_404
from cookbook.models import Recipe, Product


def index_view(request):
    products = get_list_or_404(Product)
    recipes = get_list_or_404(Recipe)
    context = {'products': products, 'recipes': recipes}
    return render(request, 'index.html', context)


def recipe_view(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    ingredients = recipe.ingredients.all()
    return render(request, 'recipe.html', {'recipe': recipe, 'ingredients': ingredients})


def page_not_found_view(request, exception, template_name='404.html'):
    context = {'message': "Страница не найдена"}
    return render(request, template_name, context, status=404)
