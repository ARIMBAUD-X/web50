from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("random", views.random, name="random"),
    path("new", views.new, name="new"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("<str:title>", views.page, name="page")
]
