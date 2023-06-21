from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from common import GetViewSet
from .models import Dungeon
from .serializers import DungeonSerializer

# Create your views here.


class DungeonAPIView(GetViewSet):
    queryset = Dungeon.objects.all()
    serializer_class = DungeonSerializer

    # def get(self, request):
    #     dungeons = Dungeon.objects.filter().prefetch_related(
    #         "desc_cabinet",
    #         "desc_cabinet__description",
    #         "skill_cabinet",
    #         "skill_cabinet__skill",
    #     )
    #     serializer = DungeonSerializer(dungeons, many=True)

    #     return Response(data=serializer.data, status=status.HTTP_200_OK)
