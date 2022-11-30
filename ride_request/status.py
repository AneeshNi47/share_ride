from django.db import models


class StatuOfRequest(models.TextChoices):
    NEW = 'New',
    ACCEPTED = 'Accepted',
    REJECTED = 'Rejected',