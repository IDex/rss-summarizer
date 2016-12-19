from django.db import models
from django.contrib.auth.models import User

class Feed(models.Model):
    url = models.CharField(max_length=1000)

class FeedSet(models.Model):
    feeds = models.ManyToManyField(Feed)

class UserInfo(models.Model):
    user = models.ForeignKey(User)
    input = FeedSet()
    output = FeedSet()
    model = models.CharField(max_length=10000)
