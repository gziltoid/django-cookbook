from django.urls import path
from cookbook import views


urlpatterns = [
    path('', views.index_view),
    path('recipe/<int:pk>', views.recipe_view),
]
