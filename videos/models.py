from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager

class Video(models.Model):
    author = models.OneToOneField(User,related_name='author_user',on_delete=models.CASCADE)
    title = models.TextField(max_length=50)
    videourl = EmbedVideoField()  # same like models.URLField()
    create_date = models.DateTimeField(default=timezone.now)
    views = models.IntegerField()
    likes= models.ManyToManyField(User,related_name='likes', blank=True)
    dislikes= models.ManyToManyField(User,related_name='dislikes', blank=True)
    tags = TaggableManager()
    
    def __str__(self):
        return str(self.author)


    
    
    
class Comment(models.Model):
    video = models.ForeignKey(Video,related_name='video_comment', on_delete=models.CASCADE)
    author = models.ForeignKey(User,related_name='video_user' ,on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=16000)

    def __str__(self):
        return str(self.author)
        