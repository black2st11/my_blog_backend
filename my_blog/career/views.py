from common import GetViewSet
from .models import Career
from .serializers import CareerSerializer

# Create your views here.


class CarrerAPIView(GetViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer()

    # def get(self, request):
    #     careers = (
    #         Career.objects.prefetch_related("achievements")
    #         .filter()
    #         .prefetch_related(
    #             "desc_cabinet",
    #             "desc_cabinet__description",
    #             "skill_cabinet",
    #             "skill_cabinet__skill",
    #         )
    #     )
    #     serializer = CareerSerializer(careers, many=True)
    #     total = 0
    #     for i in serializer.data:
    #         if i["duration"] == 0:
    #             total += 1
    #         else:
    #             total += i["duration"]
    #     return Response(
    #         data={"data": serializer.data, "total": total}, status=status.HTTP_200_OK
    #     )
