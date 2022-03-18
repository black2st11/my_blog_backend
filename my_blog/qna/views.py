from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Question
from .serializers import QuestionSerializer
from django.core.paginator import Paginator
# Create your views here.

PAGE_COUNT = 5

class QuestionAPIView(APIView):
    def get(self, request):
        page_index = request.GET.get('page', 1)
        questions = list(Question.objects.filter().prefetch_related('answers'))
        paginator = Paginator(questions, PAGE_COUNT)
        serializer = QuestionSerializer(paginator.get_page(page_index).object_list, many=True)

        return Response(data={"data" : serializer.data, 'total_count' : paginator.count},  status=status.HTTP_200_OK)