from django.urls import path, re_path

from blog.views import user_add_news, view_one_post

urlpatterns = [
    path('profile', user_add_news, name='profile'),
    re_path(r'^post/(?P<news_id>\d+)/', view_one_post, name='post')
]
