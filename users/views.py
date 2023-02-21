from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm,UserUpadateForm,UserUpdateProfile


def Register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your Acount has been created!! Now you are able to Log In ')
            return redirect('login')
    else:
         form = UserRegisterForm()
    return render (request,'users/register.html',{'form':form})

@login_required
def Profile(request):
    u_form = UserUpadateForm(instance=request.user)
    u_profile = UserUpdateProfile(instance=request.user.profile)
    context = {'u_form':u_form,'u_profile':u_profile}
    return render (request,'users/profile.html',context)