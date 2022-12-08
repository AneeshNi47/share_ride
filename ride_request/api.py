from .models import RideRequest
from rest_framework import viewsets, permissions
from .serializers import RideRequestSerializer


class RideRequestViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = RideRequestSerializer

    def get_queryset(self):
        route_filter = self.request.GET.get("route_id")
        status_filter = self.request.GET.get("status")
        if route_filter and status_filter:
            ride_requests = RideRequest.objects.filter(user_route=route_filter, status=status_filter)
        elif route_filter:
            ride_requests = RideRequest.objects.filter(user_route=route_filter)
        elif status_filter:
            ride_requests = RideRequest.objects.filter(status=status_filter)
        else:
            ride_requests = self.request.user.Request.all()
        return ride_requests

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
