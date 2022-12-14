from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .choices import ModeOfTravel, RouteType


class UserRoute(models.Model):

    name = models.CharField(max_length=50)
    map_reference = models.CharField(max_length=60)
    mode_of_travel = models.CharField(max_length=10, choices=ModeOfTravel.choices, default=ModeOfTravel.CAR)
    date_of_travel = models.DateTimeField(default=timezone.now)
    source = models.CharField(max_length=250, default="Home")
    way_points = models.CharField(max_length=500,default="NA")
    destination = models.CharField(max_length=250, default="NA")
    route_type = models.CharField(max_length=10, choices=RouteType.choices, default=RouteType.PUBLIC)
    expiry_date = models.DateTimeField()
    created_by = models.ForeignKey(User, related_name="Routes", on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.route_type} {self.name}-{self.created_by}"
