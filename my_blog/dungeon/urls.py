from common.routers import BaseRouter
from .views import DungeonAPIView

router = BaseRouter(trailing_slash=False)
router.register("", DungeonAPIView)

urlpatterns = router.get_urls()
