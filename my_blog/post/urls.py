from .views import PostAPIView
from common.routers import BaseRouter

router = BaseRouter(trailing_slash=False)
router.register("", PostAPIView)
urlpatterns = router.get_urls()
