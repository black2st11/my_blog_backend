from .models import Question, Answer
from rest_framework import serializers

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