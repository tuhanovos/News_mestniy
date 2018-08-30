from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.models import UserCreateNews
from .forms import RegisterFormView


# Create your views here.


def index(request):
    if request.method == 'GET':
        news = UserCreateNews.objects.all()
        return render(request, 'index.html', {'news': news})
    return HttpResponse(status=405)


def register_user(request):
    if request.method == 'POST':
        form = RegisterFormView(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = RegisterFormView()
    return render(request, 'register_form.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            my_pass = form.cleaned_data.get('password')
            user = authenticate(username=username, password=my_pass)
            login(request, user)
            return redirect('/blog')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


