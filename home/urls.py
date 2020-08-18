
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home')
    , path('login', views.user_login, name='user_login')
    , path('logout', views.user_logout, name='user_logout')
    , path('signup', views.user_register, name='user_register')
    , path('notice', views.service_notice, name='service_notice')
    , path('center', views.service_center, name='service_center')
    , path('mypage', views.user_mypage, name='user_mypage')
    , path('product_add', views.product_add, name='product_add')
    , path('chat_room', views.chat_room, name='chat_room')
    , path('product_like', views.product_like, name='product_like')
    ,
]