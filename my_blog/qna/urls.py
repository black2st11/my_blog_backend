from rest_framework.routers import SimpleRouter
from .views import QuestionAPIView

router = SimpleRouter()
router.register("", QuestionAPIView)

urlpatterns = router.get_urls()
