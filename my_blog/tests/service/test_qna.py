import pytest
from rest_framework.serializers import ValidationError

from qna.serializers import (
    QuestionSerializer,
    AnswerSerializer,
    EXCEED_LIMIT_OF_TODAY_QUESTION,
)
from qna.models import Question
from common.serializers import compact_create

DUPLICATE_IP = "192.168.1.1"


@pytest.mark.django_db(transaction=True)
class TestQna:
    """
    참고로 answers 가 없는 경우 답변을 안한것으로 간주(이말은 한번이라도 답변이 달린경우 이미 응했다고 할 예정)
    """

    def test_create_question(self):
        question_obj_in = {"ip": DUPLICATE_IP, "content": "이건 질문이야"}

        serializer = compact_create(QuestionSerializer, question_obj_in)

        assert serializer.instance
        assert len(serializer.data["answers"]) == 0

    """
    현재 같은 IP가 5번을 초과하는 질문을 하는 경우에는 제한을 둔다.
    """

    def test_create_six_questions(self):
        for i in range(5):
            question_obj_in = {"ip": DUPLICATE_IP, "content": f"{i}번째 질문"}
            compact_create(QuestionSerializer, question_obj_in)

        question_obj_in = {"ip": DUPLICATE_IP, "content": "등록할 수 없는 질문"}
        serializer = QuestionSerializer(data=question_obj_in)
        with pytest.raises(ValidationError) as error:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        assert error.value.detail["ip"][0] == EXCEED_LIMIT_OF_TODAY_QUESTION

    def test_create_answer(self):
        question_obj_in = {"ip": DUPLICATE_IP, "content": "이건 질문이야"}
        question_serializer = compact_create(QuestionSerializer, question_obj_in)

        answer_obj_in = {
            "question": question_serializer.data["id"],
            "content": "이건 질문입니다.",
        }
        answer_serializer = compact_create(AnswerSerializer, answer_obj_in)
        question_serializer.instance.refresh_from_db()
        assert question_serializer.instance
        assert answer_serializer.instance
        question = Question.objects.get(id=question_serializer.instance.id)
        serializer = QuestionSerializer(question)
        assert len(serializer.data["answers"]) == 1
