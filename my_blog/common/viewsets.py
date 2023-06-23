from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin


class GetViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    pass
