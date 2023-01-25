from django.urls import path
from . import views


urlpatterns = [
    path("", views.StartingPageView.as_view(), name="index_page"),
    path("all-posts", views.AllPostsView.as_view(), name="all-posts_page"),
    path("all-posts/<slug:slug>", views.SinglePostView.as_view(), name="all-post_detail_page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]