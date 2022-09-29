from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index_page"),
    path("all-posts", views.posts, name="all-posts_page"),
    path("all-posts/<slug:slug>", views.post_detail, name="all-post_detail_page")
]