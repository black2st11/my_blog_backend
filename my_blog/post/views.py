from django.shortcuts import render
from .models import Post
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import PostSerializer
from django.core.paginator import Paginator
from django.shortcuts import render
# Create your views here.

class PostAPIView(APIView):
    def get(self, request):
        page = request.GET.get('page' , 1)
        posts = list(Post.objects.filter().prefetch_related('tag_cabinet', 'tag_cabinet__tag'))
        p = Paginator(posts, 1)
        serializer = PostSerializer(p.page(page).object_list, many=True)
        return Response(data={"data" : serializer.data, "total" : len(posts)}, status=status.HTTP_200_OK)


class PostDetailAPIView(APIView):
    def get(self, request, id):
        post = list(Post.objects.filter(id=id).prefetch_related('tag_cabinet', 'tag_cabinet__tag'))
        serializer = PostSerializer(post[0])

        return Response(data=serializer.data, status=status.HTTP_200_OK)

def Test(request):
    return render(request, 'post/test.html')