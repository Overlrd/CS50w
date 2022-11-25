from django.urls import path

from . import views

app_name = "my_wiki"
urlpatterns = [
    path("", views.index, name="index"),
    ##adding url for the entry page
    path('wiki/<str:title>', views.entry, name='entry'),
    path("search/", views.search , name='search' ),
    path("create" , views.create, name="create" ),
    path("random" , views.random_page, name="random"),
    path("edit/<str:title>" ,views.edit, name='edit')
]
