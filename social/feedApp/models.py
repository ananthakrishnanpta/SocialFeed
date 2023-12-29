from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.

# Model for a Message on the App
class Message(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # CASCADE is to ensure that the User's messages are deleted when the user is deleted.
    body = models.TextField()
    msg_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='msgs')
    
    def __str__(self):
        return self.title + ' - ' + str(self.author) # self.author is an object; str() converts it into a string
    def get_absolute_url(self): # defining the url to go to after creating a new message
        # return reverse('message-detail', args=(str(self.id)))
        return reverse('feed')
    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s - %s' %(self.post.title, self.name)