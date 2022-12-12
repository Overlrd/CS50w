from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
now = datetime.now()


class User(AbstractUser):
    pass


class Category(models.Model):
    title = models.CharField(max_length=26)
    description = models.CharField(max_length=126)
    img_url = models.CharField(max_length=126)

    def __str__(self):
        return f'Category {self.title} , {self.description}'

########## Creating auctions model

class Auction(models.Model):
    ## tables : - Title , description, user ,starting_bid , image, category and date
    
    #title a 64 max_length charfield
    title = models.CharField(max_length=64)

    #decription a 64 max_lenght charfield
    description = models.CharField(max_length=64)

    #the user that create the auction
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='owner')

    #starting _bid , and integer fiels
    starting_bid = models.IntegerField()

    #image : a charfield for the url of the image
    # wew on't store the image itself, just it's link
    image_url = models.CharField(max_length=64, blank=True)

    #category , a charfield 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    #status: opened or not
    is_open = models.BooleanField(default=True)

    #date posted
    date = models.DateTimeField(default=now)

    


    def __str__(self):
        return f'Title: {self.title} , Bid: {self.starting_bid} posted on {self.date} by {self.user}' 


######## Creating a model for bids ##########"
class Bid(models.Model):
    #fiels : bid_value, auction_id; user_id
    
    #bid value
    value = models.IntegerField()
    related_auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='auction_bids')
    related_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bids')

    def __str__(self):
        return f'{self.value} $ bid for {self.related_auction.title} by user {self.related_user.username} '


######## Creating model for comments ############
class Comment(models.Model):
    #fields : comment_text, date, user, item_related
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=128)
    related_auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='auction_comments')
    related_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    date = models.DateField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return f'comment {self.title} by {self.related_user.username} on auction {self.related_auction.title} on {self.date}'



###### Creating Watclist ######
###create a watchlist , one to many realted from user , don't 
#https://stackoverflow.com/questions/63403309/watchlist-system-on-django

class Watclist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_watchlist')
    items = models.ManyToManyField(Auction, related_name='related_watchlists')

    def __str__(self):
        return f'{self.user}"s watchlist containing {self.items}' 


###### Create notififcation model
#https://stackoverflow.com/questions/72264677/how-can-i-implement-notifications-system-in-django
""" class Notification(models.Model):
    is_read = models.BooleanField(default=False)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='related_notification')

    def __str__(self):
        return f'' """

