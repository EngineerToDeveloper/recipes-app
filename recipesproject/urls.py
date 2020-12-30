from django.contrib import admin
from django.urls import path
from recipes.views import create_recipe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/create/', create_recipe, name="create_recipe"),
]
