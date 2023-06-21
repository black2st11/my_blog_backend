from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from me.models import Me
from career.models import Career
from dungeon.models import Dungeon
from post.models import Post
from qna.models import Question
from achievement.models import Achievement
from me.serializer import MeSerializer
from career.serializers import CareerSerializer
from dungeon.serializers import DungeonSerializer
from post.serializers import PostSerializer
from qna.serializers import QuestionSerializer
from achievement.serializers import AchievementSerializer

# Create your views here.


class MainAPIView(APIView):
    def get(self, request):
        me = (
            Me.objects.all()
            .prefetch_related(
                "my_skill",
                "my_skill__skill",
                "desc_cabinet",
                "desc_cabinet__description",
            )
            .order_by("-created")
        )
        achievement = Achievement.objects.filter().prefetch_related(
            "desc_cabinet",
            "desc_cabinet__description",
            "skill_cabinet",
            "skill_cabinet__skill",
            "file_cabinet",
            "file_cabinet__file",
        )
        careers = (
            Career.objects.prefetch_related("achievements")
            .filter()
            .prefetch_related(
                "desc_cabinet",
                "desc_cabinet__description",
                "skill_cabinet",
                "skill_cabinet__skill",
            )
        )
        dungeons = Dungeon.objects.filter().prefetch_related(
            "desc_cabinet",
            "desc_cabinet__description",
            "skill_cabinet",
            "skill_cabinet__skill",
        )
        posts = list(
            Post.objects.filter().prefetch_related("tag_cabinet", "tag_cabinet__tag")
        )
        questions = list(Question.objects.filter().prefetch_related("answers"))
        me_serial = MeSerializer(me[0])
        achieve_serial = AchievementSerializer(achievement[:3], many=True)
        career_serial = CareerSerializer(careers[:3], many=True)
        dungeons_serial = DungeonSerializer(dungeons[:3], many=True)
        post_serial = PostSerializer(posts[:3], many=True)
        question_serial = QuestionSerializer(questions[:3], many=True)

        return Response(
            data={
                "me": me_serial.data,
                "achieve": achieve_serial.data,
                "career": career_serial.data,
                "dungeon": dungeons_serial.data,
                "post": post_serial.data,
                "question": question_serial.data,
            },
            status=status.HTTP_200_OK,
        )
