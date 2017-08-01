from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Quest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quests')
    name = models.CharField(max_length=80)
    description = models.TextField()

    def __str__(self):
        return self.name


class Completion(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='completions')
    date = models.DateField()

    def __str__(self):
        return self.date


class Goal(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='goals')
    interval = models.CharField(max_length=40)
    count = models.IntegerField()

    def __str__(self):
        return "%s %s".format(self.count, self.interval)

class GoalInterval(models.Model):
    name = models.CharField(max_length=20)
    interval = models.DateTimeField()


class Challenge(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    interval = models.CharField(max_length=40)
    count = models.IntegerField()