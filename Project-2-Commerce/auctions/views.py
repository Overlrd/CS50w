from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms 
from .models import User, Auction, Bid

##### Form
class NewTaskForm(forms.Form):
    title = forms.CharField(label='title')
    description = forms.CharField(label='description')
    category = forms.CharField(label='category')
    bid = forms.IntegerField(label='bid')
    img_url = forms.CharField(label='img_url')



def index(request):

    return render(request, "auctions/index.html", {
        'auctions' : Auction.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def new_listing(request):
    if request.method == "POST":
        form = request.POST
        title = form['title']
        description = form['description']
        category = form['category']
        bid = form['bid']
        img_url = form['img_url']
        current_user = request.user

        #### Create Auction

        new_auction = Auction(title = title, description = description, user = current_user, starting_bid = bid, 
        image_url = img_url, category = category)
        new_auction.save()
        print(new_auction.image_url)
        print(type(new_auction.image_url))

        return index(request)

    else:
        print('form not passed with post')
        return render(request, "auctions/new_listing.html")

def item(request, auction_id):
    #### find the current auction by the id passed triough the item url from the index

    current_auction = Auction.objects.all().get(pk = auction_id)
    #### TThe current auction's bids orderreb in decreasing order

    current_auction_bids = current_auction.auction_bids.all().order_by('-value')

    ###### usefull variables #############
    ### just find out how many bids do the current user passed  on the actual auction
    name = []
    nb = 0
    for i in current_auction_bids:
        name.append(i.related_user.username)
    for i in name:
        if request.user.username == i:
            nb += 1
    #### return the result
    return render(request, 'auctions/item.html',{
        'current_auction' : current_auction,
        'current_auction_bids' : current_auction_bids,
        'current_auction_bids_by_user' : nb
    })

def pass_bid(request):
    if request.method == "POST":
        bid_value = request.POST['bid_value']
        next = request.POST.get('next','/')
        auction_id = request.POST['current_auction']
        related_auction = Auction.objects.all().get(pk = auction_id)

        new_bid = Bid(value=bid_value, related_auction = related_auction, related_user = request.user)
        new_bid.save()

        return HttpResponseRedirect(next)