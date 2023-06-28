from .views import HunterAPIView
from common.routers import BaseRouter

router = BaseRouter(trailing_slash=False)
router.register("", HunterAPIView)
urlpatterns = router.get_urls()
