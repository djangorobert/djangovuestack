from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from listing.models import Post
from django.contrib.auth.models import User
from listing.serializers import PostSerializer, UserSerializer
from rest_framework import generics
# Create your views here.
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

  

    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostList(generics.ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
