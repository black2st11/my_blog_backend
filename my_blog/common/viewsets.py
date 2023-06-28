from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin


class GetViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    pass


class IpMixin(GenericViewSet):
    def initialize_request(self, request, *args, **kwargs):
        http_request = super().initialize_request(request, *args, **kwargs)
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        try:
            _mutable = http_request.data._mutable
            http_request.data._mutable = True
            http_request.data.update({"ip": ip})
            http_request.data._mutable = _mutable
        except AttributeError:
            http_request.data.update({"ip": ip})
        return http_request
