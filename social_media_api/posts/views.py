from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend 

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at') 
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from django_filters.rest_framework import DjangoFilterBackend


from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        following_users = request.user.following.all() 
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at') 
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            post = Post.generics.get_object(pk=pk)
            like, created = Like.objects.get_or_create(user=request.user, post=post)
            
            if created:
                # Send notification to the post author
                Notification.objects.create(
                    recipient=post.author,
                    actor=request.user,
                    verb='liked your post',
                    target=post
                )
                return Response({"message": "Post liked!"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "You already liked this post!"}, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({"message": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        try:
            post = Post.generics.get_object(pk=pk)
            like = Like.objects.filter(user=request.user, post=post).first()
            if like:
                like.delete()
                return Response({"message": "Post unliked!"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "You haven't liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({"message": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

