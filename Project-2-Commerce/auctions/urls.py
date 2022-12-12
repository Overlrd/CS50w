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
    path('bid', views.pass_bid, name='bid'),
    #add comment
    path('comment', views.add_comment, name='comment'),
    #add or remove item from watchlist
    path('update_watchlist', views.update_watchlist, name='update_watchlist'),
    #show user watchlist
    path("watchlist", views.watchlist , name="watchlist"),
    #close an auction
    path('close', views.close_auction, name='close'),
    #notification content
    path('toast', views.toast, name='toast'),
    #category page
    path('category', views.category, name='category')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

