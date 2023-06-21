from rest_framework.routers import SimpleRouter
from .views import PostAPIView

router = SimpleRouter()
router.register("", PostAPIView)
urlpatterns = router.get_urls()
