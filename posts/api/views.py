from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from posts.models import Post
from posts.api.serializers import PostSerializer  
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from posts.api.permissions import IsadminOrReadOnly

class PostModelViewSet(ModelViewSet):
    permission_classes= [IsadminOrReadOnly]
    serializer_class=PostSerializer
    queryset = Post.objects.all()
    #http_method_names = ['get']

















# class PostViewSet(ViewSet):
#     def list(self, request):
#         serializer = PostSerializer(Post.objects.all(), many=True)  
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
    
#     def retrive(self, request, title):
#         post= PostSerializer(Post.objects.get(title=title))
#         return Response(status=status.HTTP_200_OK, data=post.data)


#     def create(self, request):
#         serializer = PostSerializer(data=request.POST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
    







# class PostApiView(APIView):
#     def get(self, request):
#         serializer = PostSerializer(Post.objects.all(), many=True)  
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
    
#     def post(self, request):
#         serializer = PostSerializer(data=request.POST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_200_OK, data=serializer.data)