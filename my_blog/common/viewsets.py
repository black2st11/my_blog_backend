from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin


class GetViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    pass


class IpMixin(GenericViewSet):
    def initialize_request(self, request, *args, **kwargs):
        http_request = super().initialize_request(request, *args, **kwargs)
        if request.method == "GET":  # method get 인 경우 _mutable attr 이 없음
            return http_request

        _mutable = http_request.data._mutable
        http_request.data._mutable = True
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        http_request.data.update({"ip": ip})
        http_request.data._mutable = _mutable
        return http_request
