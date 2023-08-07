from django.urls import path 
from .views import *


urlpatterns = [
    path('',index,name='index'),
    path('settings',settings,name='setting'),
    path('like_post',like_post,name='like_post'),
    path('follow',follow,name='follow'),
    path('profile/<str:sk>',profile,name='profile'),
    path('signup',signup,name='signup'),
    path('login',signin,name='signin'),
    path('upload',upload,name='upload'),
    path('search',search,name='search'),
]
