from common import GetViewSet, IpMixin
from rest_framework.mixins import CreateModelMixin
from rest_framework.pagination import PageNumberPagination

from .models import Question
from .serializers import QuestionSerializer

# Create your views here.
PAGE_COUNT = 5


class QuestionPagination(PageNumberPagination):
    page_size = PAGE_COUNT


class QuestionAPIView(IpMixin, CreateModelMixin, GetViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    pagination_class = QuestionPagination
