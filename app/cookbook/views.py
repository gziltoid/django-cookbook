from cookbook.models import Recipe, Product
from django.shortcuts import render, get_object_or_404


def index_view(request):
    if request.session:
        request.session.clear()

    if request.method == "POST":
        requested_title = request.POST.get("recipe_name")
        requested_products = list(map(int, request.POST.getlist("ingredients[]")))

        request.session["title"] = requested_title
        request.session["products"] = requested_products
        request.session.modified = True

        recipes = Recipe.objects.query(requested_title, requested_products)
    else:
        recipes = Recipe.objects.all()

    products = Product.objects.all()
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
