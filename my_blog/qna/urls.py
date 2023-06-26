from rest_framework.routers import SimpleRouter
from .views import QuestionAPIView

router = SimpleRouter(trailing_slash=False)
router.register("", QuestionAPIView)

urlpatterns = router.get_urls()
