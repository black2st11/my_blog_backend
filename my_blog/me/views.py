from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from common import GetViewSet
from .models import Me, Archiving
from .serializer import MeSerializer, ArchinvingSerializer

# Create your views here.


class MeAPIView(GetViewSet):
    queryset = Me.objects.all()
    serializer_class = MeSerializer

    # def get(self, request):
    #     me = Me.objects.all().prefetch_related('my_skill' , 'my_skill__skill', 'desc_cabinet', 'desc_cabinet__description')
    #     archiving = Archiving.objects.all().prefetch_related('desc_cabinet', 'desc_cabinet__description')
    #     me_data = MeSerializer(me[0])
    #     archiving_serializer = ArchinvingSerializer(archiving, many=True)
    #     return Response(data={"me" : me_data.data, "archiving" : archiving_serializer.data}, status=status.HTTP_200_OK)
