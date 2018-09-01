from django.urls import path

from blog.views import register_user, login_user, user_add_news

urlpatterns = [
    path('profile', user_add_news, name='profile')
]
