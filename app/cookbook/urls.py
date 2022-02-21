from cookbook import views
from django.urls import path

urlpatterns = [
    path('', views.index_view, name='index'),
    path('recipe/<int:pk>', views.recipe_view, name='recipe'),
]
