from common.routers import BaseRouter
from .views import QuestionAPIView

router = BaseRouter(trailing_slash=False)
router.register("", QuestionAPIView)

urlpatterns = router.get_urls()
