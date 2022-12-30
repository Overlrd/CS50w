from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)



## A model for posts 
## fields : user, content, date
#likes are stored in a different model
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=280)
    date = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.username,
            "body": self.content,
            "timestamp": self.date.strftime("%b %d %Y, %I:%M %p"),
            "likes" :  len(self.related_likes.all())
        }

    def __str__(self):
        return f'post {self.pk} by {self.user.username} on {self.date}'


## A model for likes 
# fields, user, post
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post, related_name="related_likes")

    def __str__(self):
        return f'like {self.pk} by {self.user}'
