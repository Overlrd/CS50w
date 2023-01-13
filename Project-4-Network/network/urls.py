
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    #add post url
    path("posts/<str:action>", views.new_post, name="new_post"),
    #get posts
    path("posts/<str:which>/<int:page>", views.posts, name="posts"),
    #get user profile infos
    path("profile/<str:username>", views.profile_page, name='profile'),
    path("follow", views.follow_or_not, name="follows"),
    #like or unlike a post
    path("like", views.like_unlike, name="like_unlike")
    ]
