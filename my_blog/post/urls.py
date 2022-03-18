from django.urls import path
from .views import PostAPIView, PostDetailAPIView, Test

urlpatterns = [
    path('/<int:id>', PostDetailAPIView.as_view()),
    path('', PostAPIView.as_view()),
    path('/test', Test )
]