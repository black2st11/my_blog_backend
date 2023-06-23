from rest_framework.serializers import Serializer


def compact_create(serializer, obj):
    serializer_obj = serializer(data=obj)
    serializer_obj.is_valid(raise_exception=True)
    serializer_obj.save()
    return serializer_obj
