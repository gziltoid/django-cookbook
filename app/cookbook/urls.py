from django.urls import path
from cookbook import views


urlpatterns = [
    path('', views.index),
    path('recipe/<int:pk>', views.recipe),
]
