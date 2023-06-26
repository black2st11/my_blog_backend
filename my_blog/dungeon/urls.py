from rest_framework.routers import SimpleRouter

from .views import DungeonAPIView

router = SimpleRouter(trailing_slash=False)
router.register("", DungeonAPIView)

urlpatterns = router.get_urls()
