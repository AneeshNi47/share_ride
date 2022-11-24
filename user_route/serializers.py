from rest_framework import serializers
from user_route.models import UserRoute


class UserRouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRoute
        fields = '__all__'