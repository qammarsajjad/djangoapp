from django.urls import path
from .views import PostListView,PostDetail
from . import views

urlpatterns = [
    path('',PostListView.as_view(),name= 'blog-home'),
    path('post-detail/<int:pk>/',PostDetail.as_view(),name= 'post-detail'),
    path('about/',views.About,name= 'blog-about'),
]
