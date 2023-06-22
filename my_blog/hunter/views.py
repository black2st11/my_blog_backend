from common import GetViewSet
from .models import Hunter
from .serializer import HunterSerializer

# Create your views here.


class HunterAPIView(GetViewSet):
    queryset = Hunter.objects.all()
    serializer_class = HunterSerializer

    # def get(self, request):
    #     me = Me.objects.all().prefetch_related('my_skill' , 'my_skill__skill', 'desc_cabinet', 'desc_cabinet__description')
    #     archiving = Archiving.objects.all().prefetch_related('desc_cabinet', 'desc_cabinet__description')
    #     me_data = MeSerializer(me[0])
    #     archiving_serializer = ArchinvingSerializer(archiving, many=True)
    #     return Response(data={"me" : me_data.data, "archiving" : archiving_serializer.data}, status=status.HTTP_200_OK)
