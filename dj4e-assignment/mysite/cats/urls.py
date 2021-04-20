from django.urls import path

from . import views

app_name = 'cats'

urlpatterns = [
    # Route: /cats/
    path('', views.CatList.as_view(), name='all'),

    # Route: /cats/main/create/
    path('main/create/', views.CatCreate.as_view(), name='cat_create'),

    # Route: /cats/main/<int:pk>/update/
    path('main/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),

    # Route: /cats/main/<int:pk>/delete/
    path('main/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),


    # Route: /breeds/
    path('breeds/', views.BreedList.as_view(), name='breed_list'),

    # Route: /breeds/main/create/
    path('breeds/create/', views.BreedCreate.as_view(), name='breed_create'),

    # Route: /breeds/main/<int:pk>/update/
    path('breeds/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),

    # Route: /breeds/main/<int:pk>/delete/
    path('breeds/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed_delete'),


]