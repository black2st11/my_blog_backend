from common.routers import BaseRouter
from .views import CarrerAPIView


router = BaseRouter(trailing_slash=False)
router.register("", CarrerAPIView)

urlpatterns = router.get_urls()
