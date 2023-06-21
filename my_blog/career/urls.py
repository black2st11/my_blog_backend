from rest_framework.routers import SimpleRouter

from .views import CarrerAPIView


router = SimpleRouter()
router.register("", CarrerAPIView)

urlpatterns = router.get_urls()
