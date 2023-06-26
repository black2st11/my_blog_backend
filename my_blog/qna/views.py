from common import GetViewSet, IpMixin
from rest_framework.mixins import CreateModelMixin
from .models import Question
from .serializers import QuestionSerializer

# Create your views here.

PAGE_COUNT = 5


class QuestionAPIView(IpMixin, CreateModelMixin, GetViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
