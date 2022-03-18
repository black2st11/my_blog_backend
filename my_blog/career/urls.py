from django.urls import path
from .views import CarrerAPIView

urlpatterns = [path('', CarrerAPIView.as_view())]