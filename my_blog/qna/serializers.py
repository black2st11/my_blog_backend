from .models import Question, Answer
from rest_framework import serializers
from datetime import datetime
from django.utils import timezone
class  AnswerSerializer(serializers.ModelSerializer):
    class Meta :
        model = Answer
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = "__all__"

    def get_answer(self, obj):
        answer_list = obj.answers.all()
        return [{'content' : answer.content for answer in answer_list}]

class QuestionCreateSerializer(serializers.Serializer):
    content = serializers.CharField()
    ip = serializers.CharField()

    def create(self, validated_data):
        return Question.objects.create(content=validated_data['content'], ip= validated_data['ip'])

    def validate_ip(self, value):
        today =datetime.now(tz=timezone.utc).today()
        start_today = f'{today.year}-{today.month}-{today.day} 00:00:00'
        end_today = f'{today.year}-{today.month}-{today.day} 23:59:59'
        today_exist_quesiton_count = Question.objects.filter(ip=value, created_at__gte=start_today, created_at__lte= end_today).count()
        if today_exist_quesiton_count > 5 :
            raise serializers.ValidationError('오늘 5개의 질문을 등록하셨습니다.')
             
        return value 