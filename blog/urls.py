from django.urls import path
from .views import PostListView,PostDetail,PostCreateView,PostUpdateView,PostDelete
from . import views

urlpatterns = [
    path('',PostListView.as_view(),name= 'blog-home'),
    path('post-detail/<int:pk>/',PostDetail.as_view(),name= 'post-detail'),
    path('post-new/',PostCreateView.as_view(),name= 'post-create'),
    path('post-update/<int:pk>/',PostUpdateView.as_view(),name= 'post-update'),
    path('post-delete/<int:pk>/',PostDelete.as_view(),name= 'post-delete'),
    path('about/',views.About,name= 'blog-about'),
]
