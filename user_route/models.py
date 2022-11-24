from django.db import models
from django.contrib.auth.models import User


class UserRoute(models.Model):
    name = models.CharField(max_length=50)
    map_reference = models.CharField(max_length=60)
    expiry_date = models.DateTimeField()
    created_by = models.ForeignKey(User, related_name="Routes", on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
