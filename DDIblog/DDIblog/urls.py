"""DDIblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from blog.views import home, login_user, logout_user, register, add_post, show_post
from django.contrib import admin

urlpatterns = [
    url(r'^$', login_user, name='login'),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'^blog/$', home, name='home'),
    url(r'^register/$', register, name='register'),
    url(r'^add_post/$', add_post, name='add post'),
    url(r'^blog/(?P<post_id>\d+)/$', show_post, name='show post'),
    # url(r'^blog/comment/(?P<post_id>\d+)/$', add_comment, name='add_comment'),
    url(r'^admin/', include(admin.site.urls)),
]
