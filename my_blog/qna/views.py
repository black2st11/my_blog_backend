from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Question
from .serializers import QuestionSerializer, QuestionCreateSerializer
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


    def post(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        prev_data = request.data
        prev_data['ip'] = ip
        print(request.data)
        serializer = QuestionCreateSerializer(data=prev_data)
        print(serializer.is_valid())
        serializer.create(serializer.validated_data)
        return Response(data={"data" : 200 },  status=status.HTTP_200_OK)
