from user_route.models import UserRoute
from rest_framework import viewsets, permissions
from .serializers import UserRouteSerializer


class UserRouteViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = UserRouteSerializer

    def get_queryset(self):
        return self.request.user.leads.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
