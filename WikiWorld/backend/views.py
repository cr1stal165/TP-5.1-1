from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Topic, Article
from .serializers import UserSerializer, TopicSerializer, ArticleSerializer
from django.views.generic import TemplateView


class UserList(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserListView(TemplateView):
    template_name = 'index.html'


class TopicList(APIView):

    def get(self, request):
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)


class TopicListView(TemplateView):
    template_name = 'topics.html'


class ArticleList(APIView):

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class ArticleListView(TemplateView):
    template_name = 'articles.html'