"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

import backend.views

urlpatterns = [
    path('', backend.views.welcome, name='welcome'),
    path('dashboard/', backend.views.dashboard, name='dashboard'),
    path('login/', LoginView.as_view(template_name='login.html'),name='login' ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls, name='admin'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))
