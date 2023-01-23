from django.urls import path
from listing.views import *

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view(), name='user-detail'),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    
 
]