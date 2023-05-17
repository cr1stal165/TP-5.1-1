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
from django.urls import path, include, re_path
from backend.views import ArticleAPIList, ArticleAPIUpdateView, ArticleAPIDestroyView, RegistrUserView, \
    TokenCreateViewApi, TopicAPIList, ArticleDetailView, UsersDetailView
from frontend.urls import urlpatterns1
from WikiWorld import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/drf-auth/', include('rest_framework.urls')),
    # path('api/v1/articles-full/', ArticleAPIList1.as_view()),
    path('api/v1/articles/', ArticleAPIList.as_view()),
    path('api/v1/article/<int:pk>/', ArticleDetailView.as_view()),
    path('api/v1/articles/<int:pk>/', ArticleAPIUpdateView.as_view()),
    path('api/v1/articles/delete/<int:pk>/', ArticleAPIDestroyView.as_view()),
    path('api/v1/registration/', RegistrUserView.as_view()),
    path('api/v1/login/', TokenCreateViewApi.as_view()),

    path('api/v1/topics/', TopicAPIList.as_view()),

    path('api/v1/user/<int:pk>/', UsersDetailView.as_view()),

    # path('api/v1/updatepassword/', UpdatePasswordUserView.as_view()),
    # path('api/v1/auth/', include('djoser.urls')),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),
]

urlpatterns += urlpatterns1


if settings.DEBUG:
    urlpatterns += static(
            settings.STATIC_URL,
            document_root=settings.STATIC_ROOT
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
