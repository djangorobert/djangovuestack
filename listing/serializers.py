from rest_framework import routers, serializers, viewsets
from listing.models import *

# Serializers define the API representation.
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    #posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username']
class PostSerializer(serializers.HyperlinkedModelSerializer):
    #users = UserSerializer(many=True, read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'bedroom', 'city', 'price', 'pub_date', 'author']
       

   