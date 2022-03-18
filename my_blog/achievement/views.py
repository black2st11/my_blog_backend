from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AchievementSerializer
from .models import Achievement

# Create your views here.

class AchievementAPIView(APIView):
    def get(self, request):
        achievement = Achievement.objects.filter().prefetch_related('desc_cabinet' , 'desc_cabinet__description', 'skill_cabinet' , 'skill_cabinet__skill', 'file_cabinet', 'file_cabinet__file')
        serializer = AchievementSerializer(achievement, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
