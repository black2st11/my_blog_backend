from django.urls import path
from .views import MeAPIView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("", MeAPIView)
urlpatterns = router.get_urls()
