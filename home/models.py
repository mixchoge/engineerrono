from django.db import models
from django.contrib.auth.models import User


class Respond(models.Model):
    img = models.ImageField(upload_to='pics')
    comment = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=300)


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()


class Chat(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()


class Private(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
