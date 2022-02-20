from django.shortcuts import render, get_object_or_404, get_list_or_404
from cookbook.models import Recipe, Product, Ingredient
from django.db.models import Q
from functools import reduce


def index_view(request):
    products = get_list_or_404(Product)
    recipes = []
    query = {}

    if request.method == "POST":
        recipe_title_part = request.POST.get("recipe_name")
        selected_product_indices = request.POST.getlist("ingredients[]")

        if selected_product_indices:
            recipe_ids = (
                Ingredient.objects
                .filter(product_id__in=selected_product_indices)
                .values("recipe")
                .distinct()
            )
            query["id__in"] = recipe_ids

        if recipe_title_part:
            query["title__icontains"] = recipe_title_part

    recipes = Recipe.objects.filter(**query)

    return render(request, "index.html", {"products": products, "recipes": recipes})


def recipe_view(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    ingredients = recipe.ingredients.all()
    return render(
        request, "recipe.html", {"recipe": recipe, "ingredients": ingredients}
    )


def page_not_found_view(request, exception, template_name="404.html"):
    context = {"message": "Страница не найдена"}
    return render(request, template_name, context, status=404)
