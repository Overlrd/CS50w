import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist


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
        try :

            if len(request_user.related_follows.get().followed_users.filter(pk = user.pk)) > 0 :
                json_response['following'] = True
            else:
                json_response['following'] = False
        except ObjectDoesNotExist:
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
def new_post(request, action):
    if action == "add":
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
    elif action == "edit":
                #assert the post method
        if request.method != "POST":
            return JsonResponse({"error": "POST request required"}, status=400)

        # get the content of the post 
        data = json.loads(request.body)
        post_content = data.get("body", "")
        post_id = data.get("tweet", "")
        post_user = request.user

        post_to_edit = Post.objects.get(pk = int(post_id))

        #if the request user own the post :
        if str(post_user) == str(post_to_edit.user): 
            print(f'should update post {post_to_edit.user} by {post_user}')
            try:

                post_to_edit.content = post_content
                post_to_edit.save()
                print('post updated')
                return JsonResponse({"message": "Post added successfully"}, status=201)

            except Exception as e:
                print(e)
                return JsonResponse({"error": "Error editing post"}, status=400)


        else :
        #if the request user dont own the post
            print('this user cant update this post ')
            return JsonResponse({"error": "Action not allowed for current user "}, status=400)
    else :
            return JsonResponse({"error": "Inexisting Route"}, status=400)

        


# view all postsr
def posts(request, which, page):
    json_response = {}
    if which == 'all':
        posts_to_return = Post.objects.all()
        posts_to_return = posts_to_return.order_by("-date")
        posts_response = [post.serialize() for post in posts_to_return]
        #use paginator
        p = Paginator(posts_response, 10)
        page1 = p.page(page)
        json_response['posts'] = page1.object_list
        json_response['num_pages'] = p.num_pages
        return JsonResponse(json_response, safe=False)

    elif which == "following":
        json_response = {}
        posts_list = []
        user = request.user
        #get all followed user's
        followed_users = user.related_follows.get().followed_users.all()
        for i in followed_users:
            all_posts = i.related_posts.all()
            for i in all_posts:
                posts_list.append(i)

        posts_response = [post.serialize() for post in posts_list]
        p = Paginator(posts_response, 10)
        page1 = p.page(page)
        json_response['posts'] = page1.object_list
        json_response['num_pages'] = p.num_pages
        return JsonResponse(json_response, safe=False)

    else :
        try:
            user = User.objects.get(username = which)
            posts_to_return = user.related_posts.all()
            posts_response = [post.serialize() for post in posts_to_return]

            p = Paginator(posts_response, 10)
            page1 = p.page(page)
            json_response['posts'] = page1.object_list
            json_response['num_pages'] = p.num_pages
            print(json_response)
            return JsonResponse(json_response, safe=False)

        except Exception as e:
            print(e)
            return JsonResponse({"message": e}, status=404)




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


@csrf_exempt
@login_required 
def like_unlike(request):
    if request.method == "POST":
                # get the content of the request
        data = json.loads(request.body)
        action = data.get("action", "")
        post_id = data.get("tweet", "")

        if action == "like":
            try:
                user_likes_list , created = Like.objects.get_or_create(user = request.user)
                user_likes_list.posts.add(post_id)
                return JsonResponse({"message" : "Post liked "}, status=201)
            except Exception as e :
                print(e)
                return JsonResponse({"error" : " error processing this action "}, status=400)

        elif action == "unlike":
            try :
                user_likes_list = Like.objects.get(user = request.user )
                user_likes_list.posts.remove(post_id)

                return JsonResponse({"message" : "Post Unliked "}, status=201)
            except Exception as e :
                print(e)
                return JsonResponse({"error" : " error processing this action "}, status=400)
        else :

            return JsonResponse({"error" : " action should be 'like' or 'unlike' "}, status=400)

