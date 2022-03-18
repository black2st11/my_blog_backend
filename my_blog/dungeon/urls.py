from django.urls import path
from .views import DungeonAPIView

urlpatterns = [path('', DungeonAPIView.as_view())]