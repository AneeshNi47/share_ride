from rest_framework import routers
from .api import UserRouteViewSet

router = routers.DefaultRouter()
router.register('api/user_routes', UserRouteViewSet, 'UserRoutes')

urlpatterns = router.urls
