import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Post, Like


def index(request):
    return render(request, "network/index.html")


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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username ,email, password, first_name = first_name, last_name=last_name)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


# add a new post

@csrf_exempt
@login_required
def new_post(request):
    #assert the post method
    if request.method != "POST":
        return JsonResponse({"error": "POST request required"}, status=400)

    # get the content of the post 
    data = json.loads(request.body)
    post_content = data.get("body", "")
    post_user = request.user

    new_post = Post(user = post_user, content = post_content)
    new_post.save()
    print(new_post)

    return JsonResponse({"message": "Post added successfully"}, status=201)


# view all posts
def posts(request, which):
    if which == 'all':
        posts_to_return = Post.objects.all()
        posts_to_return = posts_to_return.order_by("-date")
        json_object = [post.serialize() for post in posts_to_return]
        return JsonResponse(json_object, safe=False)

def profile(request, username):
    return render(request, "network/profile.html",{
        'username':username
    })