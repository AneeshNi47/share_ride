from django.db import models


class ModeOfTravel(models.TextChoices):
    CAR = 'Car',
    BIKE = 'BIKE',
    SUV = 'SUV',
    OTHERS = 'Others',


class RouteType(models.TextChoices):
    PRIVATE = 'Private',
    PUBLIC = 'Public'
