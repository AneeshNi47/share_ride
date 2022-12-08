from rest_framework import viewsets, permissions
from django.contrib.auth.models import Group
from .serializers import CreateTeamSerializer

class TeamViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = CreateTeamSerializer

    def get_queryset(self):
        all_groups = Group.objects.all()
        for group in all_groups:
            group = Group.objects.get(id=group.id)
            users = group.user_set.all()
            print(users)
        return all_groups