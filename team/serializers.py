from rest_framework import serializers
from django.contrib.auth.models import Group


class CreateTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id','name')