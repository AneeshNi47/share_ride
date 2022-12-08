from rest_framework import routers
from .api import RideRequestViewSet

router = routers.DefaultRouter()
router.register('api/ride_request', RideRequestViewSet, 'RideRequests')

urlpatterns = router.urls
