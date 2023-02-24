from django.shortcuts import render
from django.views.generic import ListView,DeleteView
from .models import Post





def Home(request):
    context  = {'posts':Post.objects.all}
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    
    ordering = ['-date_posted']

class PostDetail(DeleteView):
    model = Post
    template_name = 'blog/post_detail.html'

def About(request):
   return render(request,'blog/about.html',{'title':'About'})
