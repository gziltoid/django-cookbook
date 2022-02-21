from django.shortcuts import render, get_object_or_404, get_list_or_404
from cookbook.models import Recipe, Product, Ingredient
from django.db.models import Count


def index_view(request):
    products = get_list_or_404(Product)
    recipes = []
    query = {}

    request.session.clear()

    if request.method == "POST":
        requested_title = request.POST.get("recipe_name")
        request.session['title'] = requested_title
        requested_products = list(map(int, request.POST.getlist("ingredients[]")))
        request.session['products'] = requested_products

        if requested_products:
            recipe_ids = (
                Ingredient.objects
                .filter(product_id__in=requested_products)
                .values('recipe')
                .annotate(count=Count('recipe'))
                .filter(count__exact=len(requested_products))
                .values('recipe')
            )
            query["id__in"] = recipe_ids

        if requested_title:
            query["title__icontains"] = requested_title

    recipes = Recipe.objects.filter(**query)
    context = {"products": products, "recipes": recipes}
    return render(request, "index.html", context)


def recipe_view(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    ingredients = recipe.ingredients.all()
    return render(
        request, "recipe.html", {"recipe": recipe, "ingredients": ingredients}
    )


def page_not_found_view(request, exception, template_name="404.html"):
    context = {"message": "Страница не найдена"}
    return render(request, template_name, context, status=404)
