from common.routers import BaseRouter
from .views import AchievementAPIView

router = BaseRouter(trailing_slash=False)
router.register("", AchievementAPIView)

urlpatterns = router.get_urls()
