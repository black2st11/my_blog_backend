from rest_framework.routers import SimpleRouter
from .views import PostAPIView

router = SimpleRouter(trailing_slash=False)
router.register("", PostAPIView)
urlpatterns = router.get_urls()
