from rest_framework import routers
from .api import RideRequestViewSet

router = routers.DefaultRouter()
router.register('api/ride_requests', RideRequestViewSet, 'RideRequests')

urlpatterns = router.urls
