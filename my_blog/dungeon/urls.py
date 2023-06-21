from rest_framework.routers import SimpleRouter

from .views import DungeonAPIView

router = SimpleRouter()
router.register("", DungeonAPIView)

urlpatterns = router.get_urls()
