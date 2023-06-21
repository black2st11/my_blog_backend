from common import GetViewSet
from .serializers import AchievementSerializer
from .models import Achievement


class AchievementAPIView(GetViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

    # def get(self, request):
    #     achievement = Achievement.objects.filter().prefetch_related(
    #         "desc_cabinet",
    #         "desc_cabinet__description",
    #         "skill_cabinet",
    #         "skill_cabinet__skill",
    #         "file_cabinet",
    #         "file_cabinet__file",
    #     )
    #     serializer = AchievementSerializer(achievement, many=True)
    #     return Response(status=status.HTTP_200_OK, data=serializer.data)
