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
        route_requests = RideRequest.objects.filter(user_route=route_filter) if route_filter else None
        status_requests = RideRequest.objects.filter(status=status_filter) if status_filter else None
        all_requests = self.request.user.Request.all() if not status_filter and not route_filter else None
        ride_requests = route_requests | status_requests | all_requests
        return ride_requests

    def perform_create(self, serializer):
        serializer.save(requested_by=self.request.user)
