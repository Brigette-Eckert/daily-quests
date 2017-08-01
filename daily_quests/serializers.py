from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Quest, Completion, Goal


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        quests = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        fields = ('url', 'username', 'email', 'quests')



class QuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quest
        goals = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        completions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        fields = ('user', 'name', 'description', 'goals', 'completions')


class CompletionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Completion
        fields = ('quest', 'date')


class GoalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goal
        goals = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        fields = ('quest', 'interval', 'frequency', 'count')
