from django.urls import path
from . import views

urlpatterns= [
    path('',views.index,name='index'),
    path('posts',views.post,name='post'),
    path('postview/<str:pk>',views.postview,name='postview')
]