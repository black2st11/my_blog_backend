from rest_framework.routers import SimpleRouter

from .views import AchievementAPIView

router = SimpleRouter(trailing_slash=False)
router.register("", AchievementAPIView)

urlpatterns = router.get_urls()
