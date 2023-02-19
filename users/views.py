from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm


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

