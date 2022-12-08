from user_route.models import UserRoute
from rest_framework import viewsets, permissions
from .serializers import UserRouteSerializer
from .choices import RouteType


class UserRouteViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = UserRouteSerializer

    def get_queryset(self):
        public_routes = UserRoute.objects.filter(route_type=RouteType.PUBLIC)
        all_routes = self.request.user.Routes.all()
        routes = public_routes | all_routes
        return routes

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
