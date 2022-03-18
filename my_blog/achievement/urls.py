from django.urls import path
from .views import AchievementAPIView

urlpatterns = [path('', AchievementAPIView.as_view())]