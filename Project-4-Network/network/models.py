from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass



## A model for posts 
## fields : user, content, date
#likes are stored in a different model
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=280)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'post {self.pk} by {self.user.username} on {self.date}'


## A model for likes 
# fields, user, post
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post, related_name="related_likes")

    def __str__(self):
        return f'like {self.pk} by {self.user}'
