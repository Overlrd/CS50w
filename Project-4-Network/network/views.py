import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Post, Like, Follow


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


def profile_page(request,username):
    json_response = {}
    #return username, mail, first and last name , joined date , subscribers and subscriptions, num posts
    #and all user posts 
    user = User.objects.get(username = username)

    if str(request.user) != "AnonymousUser":
        request_user = User.objects.get(username = request.user)
        #check if the request user is following the profiled user
        if len(request_user.related_follows.get().followed_users.filter(pk = user.pk)) :
            json_response['following'] = True
        else:
            json_response['following'] = False
    else:
        request_user = None

    all_posts = user.related_posts.all()
    all_posts = all_posts.order_by("-date")
    json_response['id'] = user.pk
    json_response["username"] = user.username
    json_response['first_name']  = user.first_name
    json_response['last_name'] = user.last_name
    json_response['date_joined'] = user.date_joined
    json_response['user_email'] = user.email
    json_response['num_posts'] = len(all_posts)
    json_response['post_objects'] = [post.serialize() for post in all_posts ]
    return render(request, "network/profile.html",{
        'response':json_response
    })

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


# view all postsr
def posts(request, which):
    if which == 'all':
        posts_to_return = Post.objects.all()
        posts_to_return = posts_to_return.order_by("-date")
        json_response = [post.serialize() for post in posts_to_return]
        print('all posts requested')
        return JsonResponse(json_response, safe=False)

    if which == "following":
        json_response = {}
        posts_list = []
        user = request.user
        #get all followed user's
        followed_users = user.related_follows.get().followed_users.all()
        for i in followed_users:
            all_posts = i.related_posts.all()
            for i in all_posts:
                posts_list.append(i)

        json_response = [post.serialize() for post in posts_list]
        print(posts_list)

        return JsonResponse(json_response, safe=False)



@csrf_exempt
@login_required
def follow_or_not(request):
    if request.method == "PUT":
        data = json.loads(request.body)
        followed_user = data.get("followed_user")
        followed_user_name = data.get('followed_user_name')

        if data.get("action") == "follow":
            print('following ')
            follow_list , created = Follow.objects.get_or_create(user = request.user )
            follow_list.followed_users.add(followed_user)
            return JsonResponse({"message": "followed suceesfully"}, status=201)

    
        elif data.get("action") == "unfollow":
            print("unfollowing")
            follow_list , created = Follow.objects.get_or_create(user = request.user)
            follow_list.followed_users.remove(followed_user)
            return JsonResponse({"message": " successfully"}, status=201)

    
