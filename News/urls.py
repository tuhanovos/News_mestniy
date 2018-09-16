"""News URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from blog.views import index, register_user, login_user

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index, name='index'),
                  path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
                  path('registration/', register_user, name='registration'),
                  path('login/', login_user, name='login'),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  re_path(r'^api-auth/', include('rest_framework.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]
