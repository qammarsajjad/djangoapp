from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post





def Home(request):
    context  = {'posts':Post.objects.all}
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    
    ordering = ['-date_posted']

class PostDetail(DetailView):
    model = Post
 

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.auther = self.request.user
        return super().form_valid(form)
        

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.auther = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.auther:
            return True
        return False


class PostDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    template_name = 'blog/post_form_confrim.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.auther:
            return True
        return False
   

def About(request):
   return render(request,'blog/about.html',{'title':'About'})
     

        

