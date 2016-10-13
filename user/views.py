from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm
# Create your views here.

def index(request):
    return render(request,'user/index.html',)


def register_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()

        user = authenticate(username=username , password = password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return render(request,'user/index.html')
    context  = {
        'form':form
    }
    return render(request,'user/register.html',context)

def login_user(request):
    return render(request,'user/login.html',)

