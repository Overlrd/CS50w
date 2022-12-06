from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    #create a new listing
    path("new_listing", views.new_listing , name='new_listing'),
    #listing page
    path("<int:auction_id>/item", views.item, name='item'),
    #pass bid
    path('bid', views.pass_bid, name='bid')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

