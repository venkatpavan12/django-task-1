from django.urls import path
from . import views

urlpatterns=[
    path("home",views.HomeView.as_view(),name='home'),
    path("post/<int:pk>",views.PostDetailView.as_view(),name='post-detail'),
    path("create",views.AddPostView.as_view(),name='post-add'),
    path("drafts",views.DraftView.as_view(),name='post-draft'),
    path("drafts/edit/<int:pk>",views.UpdatePost.as_view(),name='post-edit'),
    path("delete/<int:pk>",views.DeletePostView.as_view(),name='post-delete'),
    path("category/<str:cats>",views.CategoryView,name='category'),
    path("myposts",views.User_posts,name='myposts'),
]