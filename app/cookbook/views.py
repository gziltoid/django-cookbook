from django.shortcuts import render, get_object_or_404, get_list_or_404
from cookbook.models import Recipe


def index(request):
    recipes = get_list_or_404(Recipe)
    return render(request, 'index.html', {'recipes': recipes})


def recipe(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    return render(request, 'recipe.html', {'recipe': recipe})


def page_not_found_view(request, exception, template_name='404.html'):
    context = {'message': "Страница не найдена"}
    return render(request, template_name, context, status=404)
