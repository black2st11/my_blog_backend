from rest_framework.serializers import BaseSerializer, ValidationError
import datetime

START_DATE_EXCEED_END_DATE = "종료시간은 시작시간보다 앞설 수 없습니다."


def compact_create(serializer, obj):
    serializer_obj = serializer(data=obj)
    serializer_obj.is_valid(raise_exception=True)
    serializer_obj.save()
    return serializer_obj


class EndDateValidationMixin(BaseSerializer):
    def validate_end_date(self, end_date):
        start_date = datetime.date.fromisoformat(self.initial_data.get("start_date"))
        if start_date > end_date:
            raise ValidationError(START_DATE_EXCEED_END_DATE)

        return end_date
