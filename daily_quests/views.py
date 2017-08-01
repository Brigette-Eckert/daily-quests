from django.contrib.auth.models import User
from rest_framework import viewsets
from daily_quests.serializers import (UserSerializer, QuestSerializer, CompletionSerializer, GoalSerializer)
from django.shortcuts import render

from .models import Quest, Completion, Goal


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class QuestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows quests to be viewed or edited
    """
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer


class CompletionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows completions to be viewed or edited
    """
    queryset = Completion.objects.all()
    serializer_class = CompletionSerializer

class GoalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows goals to be viewed or edited
    """
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

def home(request):
    return render(request, 'home.html')