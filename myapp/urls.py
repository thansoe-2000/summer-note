from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= 'indexPage'),
    
    # create
    path('post/create', views.createPost, name='post.create'),
    path('post/detail/<str:pk>/', views.detailPost, name='post.detail'),
]
