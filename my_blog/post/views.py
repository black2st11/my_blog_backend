from common import GetViewSet
from .models import Post
from .serializers import PostSerializer

# Create your views here.


class PostAPIView(GetViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer()


#     def get(self, request):
#         page = request.GET.get("page", 1)
#         posts = list(
#             Post.objects.filter()
#             .prefetch_related("tag_cabinet", "tag_cabinet__tag")
#             .order_by("-created_at")
#         )
#         p = Paginator(posts, 10)
#         serializer = PostSerializer(p.page(page).object_list, many=True)
#         return Response(
#             data={"data": serializer.data, "total": len(posts)},
#             status=status.HTTP_200_OK,
#         )


# class PostDetailAPIView(APIView):
#     def get(self, request, id):
#         post = list(
#             Post.objects.filter(id=id).prefetch_related(
#                 "tag_cabinet", "tag_cabinet__tag"
#             )
#         )
#         serializer = PostSerializer(post[0])

#         return Response(data=serializer.data, status=status.HTTP_200_OK)


# def Test(request):
#     return render(request, "post/test.html")
