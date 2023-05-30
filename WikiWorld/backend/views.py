import datetime

from django.contrib.auth import authenticate, login, logout
from djoser import utils
from djoser.conf import settings
from djoser.serializers import TokenSerializer
from djoser.views import TokenCreateView, TokenDestroyView
from rest_framework import generics, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import Article, User, Topic
from .serializers import ArticleSerializer, UserRegistrSerializer, TopicSerializer, UserSerializer
from .permissions import IsAdminOrReadOnly


class RegistrUserView(CreateAPIView):
    queryset = User.objects.all()

    serializer_class = UserRegistrSerializer

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):

        serializer = UserRegistrSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class UpdatePasswordUserView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        curr_password = user.password
        new_password = request.data.get('password')

        if curr_password == new_password:
            return Response({'error': 'Пароли совпадают'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()

        return Response({'response': 'Пароль успешно изменен'}, status=status.HTTP_200_OK)


class TokenCreateViewApi(TokenCreateView):
    serializer_class = settings.SERIALIZERS.token_create
    permission_classes = settings.PERMISSIONS.token_create

    def _action(self, serializer):
        token = utils.login_user(self.request, serializer.user)
        token_serializer_class = settings.SERIALIZERS.token
        login(self.request, serializer.user)
        return Response(
            data=(token_serializer_class(token).data, ({"nickname": serializer.user.nickname}),({"email": serializer.user.email}), ({"is_superuser":serializer.user.is_superuser}), ({"id": serializer.user.id}),({"password": serializer.user.password})),
            status=status.HTTP_200_OK,
        )


class TokenDestroyViewApi(TokenDestroyView):

    permission_classes = settings.PERMISSIONS.token_destroy

    def post(self, request):
        utils.logout_user(request)
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleAPIList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(date=datetime.date.today())


class ArticleAPIUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)

    def perform_update(self, serializer):
        serializer.save(date=datetime.date.today())


class ArticleAPIDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)


class ArticleDetailView(APIView):
    def get(self, request, pk):
        try:
            article = Article.objects.get(id=pk)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UsersDetailView(APIView):
    def get(self, request, pk):
        try:
            article = User.objects.get(id=pk)
            serializer = UserSerializer(article)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class TopicAPIList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicAPIAdd(generics.CreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (IsAdminOrReadOnly, )


class TopicAPIDelete(generics.DestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (IsAdminOrReadOnly,)


class TopicAPIUpdate(generics.UpdateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (IsAdminOrReadOnly,)


class TopicDetailView(APIView):
    def get(self, request, pk):
        try:
            topic = Topic.objects.get(id=pk)
            serializer = TopicSerializer(topic)
            return Response(serializer.data)
        except Topic.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)