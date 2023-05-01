"""
URL configuration for WikiWorld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from backend.views import UserList, UserListView, TopicList, TopicListView, ArticleList, ArticleListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', UserList.as_view()),
    path('api/topics/', TopicList.as_view()),
    path('api/articles/', ArticleList.as_view()),
    path('', UserListView.as_view(), name='user_list'),
    path('topics/', TopicListView.as_view(), name='topics_list'),
    path('articles/', ArticleListView.as_view(), name='articles_list'),

]
