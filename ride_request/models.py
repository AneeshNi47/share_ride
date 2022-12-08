from django.db import models
from django.contrib.auth.models import User
from user_route.models import UserRoute
from .status import StatuOfRequest


class RideRequest(models.Model):
    user_route = models.ForeignKey(UserRoute, related_name="Request", on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=500)
    expiry_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=StatuOfRequest.choices, default=StatuOfRequest.NEW)
    created_by = models.ForeignKey(User, related_name="Request", on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message} {self.user_route.id}"
