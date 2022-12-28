
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    #add post url
    path("posts", views.new_post, name="new_post"),
    #get posts
    path("posts/<str:which>", views.posts, name="posts")
]
