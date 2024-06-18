from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response
from posts.models import Post
from posts.api.serializers import PostSerializer  

class PostApiView(APIView):
    def get(self, request):
        serializer = PostSerializer(Post.objects.all(), many=True)  
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        post = Post.objects.create(
            title=request.data['title'], 
            description=request.data['description'], 
            order=request.data['order']
        )
        serializer = PostSerializer(post)
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
