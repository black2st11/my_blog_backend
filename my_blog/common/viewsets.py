from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin


class GetViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    pass
