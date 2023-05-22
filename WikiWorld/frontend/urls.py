"""
URL configuration for test_lesson project.

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from frontend import views
from WikiWorld import settings

urlpatterns1 = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('topics/', views.all_topics, name='all_topics'),
    path('article_page/<int:pk>/', views.article_page, name='article_page'),
    path('articles_topic/<int:pk>/', views.articles_topic, name='articles_topic'),
    path('login/', views.login_page, name='login_page'),
    path('registration/', views.registration_page, name='registration_page'),
    path('download_pdf/', views.download_pdf, name='download_pdf'),
    path('profile/', views.profile_page, name='profile_page'),
    path('download_audio/', views.download_audio, name='download_audio'),
    path('index_auth/', views.index_auth, name='index_auth'),
    path('edit_profile_auth/', views.edit_profile_auth, name='edit_profile_auth'),
    path('article_page_auth/', views.article_page_auth, name='article_page_auth'),
    path('articles_topic_auth/', views.articles_topic_auth, name='articles_topic_auth'),
    path('all_topics_auth/', views.all_topics_auth, name='all_topics_auth'),
    path('add_article/', views.add_article, name='add_article'),
    path('edit_article/', views.edit_article, name='edit_article'),
    path('admin_thematics/', views.admin_thematics, name='admin_thematics'),
    path('admin_many_articles/', views.admin_many_articles, name='admin_many_articles'),
    path('admin_edit_article/', views.admin_edit_article, name='admin_edit_article'),
    path('admin_edit_thematics/', views.admin_edit_thematics, name='admin_edit_thematics'),
]

if settings.DEBUG:
    urlpatterns1 += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
