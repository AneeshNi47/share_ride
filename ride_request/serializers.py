from rest_framework import serializers
from .models import RideRequest


class RideRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideRequest
        fields = '__all__'

    def create(self, validated_data):
        existing_requests = RideRequest.objects.filter(user_route=validated_data['user_route'],
                                                       created_by=validated_data['created_by'])

        if len(existing_requests) != 0:
            raise serializers.ValidationError({"non_field_errors": [
                "You have already made a request for the route"
            ]})
        return RideRequest.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.message = validated_data.get('message', instance.message)
        instance.save()
        return instance