from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from blog.models import UserCreateNews
from .forms import RegisterFormView, ProfileForm


# Create your views here.


def index(request):
    if request.method == 'GET':
        news = UserCreateNews.objects.all().order_by('-news_date')
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
    if request.user.is_authenticated:
        return redirect('/')
    else:
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


def user_add_news(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                text = form.cleaned_data['text']
                news = UserCreateNews(title=title, news_text=text)
                news.save()
                return redirect('/')
        else:
            form = ProfileForm()
            return render(request, 'blog/profile.html', {'form': form})
    else:
        return redirect('/login')


def view_one_post(request, news_id):
    post = UserCreateNews.objects.get(pk=news_id)
    return render(request, 'blog/post.html', {'post': post})
