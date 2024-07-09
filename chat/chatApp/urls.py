from django.contrib import admin
from django.urls import path, include
from .views import index, post_queries


urlpatterns = [
    path("", index, name="index"),
    path("post_queries/", post_queries, name="post_queries"),
]
