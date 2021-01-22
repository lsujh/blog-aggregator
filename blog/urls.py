from django.urls import path

from . import views
from comments.views import CommentCreate
from .feeds import LatestPostsFeed

app_name = "blog"

urlpatterns = [
    path("tag/<slug:tag_slug>/", views.BlogListView.as_view(), name="post_list_by_tag"),
    path("<int:post_id>/share/", views.post_share, name="post_share"),
    path("feed/", LatestPostsFeed(), name="post_feed"),
    path("<slug:category>/<slug:slug>/comment-create/", CommentCreate.as_view(), name="comment_create"),
    path('<int:pk>/edit/', views.BlogUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete'),
    path('new/', views.BlogCreateView.as_view(), name='post_new'),
    path("<slug:category>/", views.BlogListView.as_view(), name="post_list"),
    path('<slug:category>/<slug:slug>/', views.BlogDetailView.as_view(), name='post_detail'),
    path('', views.BlogListView.as_view(), name='post_list'),
]
