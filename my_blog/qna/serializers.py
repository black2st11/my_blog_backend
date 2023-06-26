from rest_framework import serializers
from django.utils import timezone
from datetime import datetime, time

from .models import Question, Answer


EXCEED_LIMIT_OF_TODAY_QUESTION = "오늘 5개의 질문을 등록하셨습니다."


def create_start_end_date():
    now = datetime.now()
    start_date = timezone.make_aware(datetime.combine(now, time.min))
    end_date = timezone.make_aware(datetime.combine(now, time.max))
    return start_date, end_date


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["question", "id", "content"]


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = ["id", "ip", "content", "answers"]

    def validate_ip(self, data):
        start_date, end_date = create_start_end_date()
        today_exist_quesiton_count = Question.objects.filter(
            ip=data, created__gte=start_date, created__lte=end_date
        ).count()
        if today_exist_quesiton_count >= 5:
            raise serializers.ValidationError(EXCEED_LIMIT_OF_TODAY_QUESTION)

        return data
