from django.urls import path
from .views import HunterAPIView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("", HunterAPIView)
urlpatterns = router.get_urls()
