import datetime
from django.contrib.auth import login, logout
from djoser import utils
from djoser.conf import settings
from djoser.views import TokenCreateView, TokenDestroyView
from rest_framework import generics, status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Article, User, Topic
from .serializers import ArticleSerializer, UserRegistrSerializer, TopicSerializer, UserSerializer
from .permissions import IsAdminOrReadOnly
from .swagger_docs import topic_detail_get, topic_patch, topic_put, topic_delete, topic_post, topic_get_all, \
    article_get_all, article_post, article_put, article_patch, article_delete, article_detail_get, get_user, login_user, \
    logout_user, registration_user, update_password_put, update_password_patch


class RegistrUserView(CreateAPIView):
    queryset = User.objects.all()

    serializer_class = UserRegistrSerializer

    permission_classes = [AllowAny]

    @registration_user
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

    @update_password_patch
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @update_password_put
    def put(self, request, *args, **kwargs):
        user = request.user
        curr_password = user.password
        new_password = request.data.get('password')
        new_nickname = request.data.get('nickname')
        if curr_password == new_password:
            return Response({'error': 'Пароли совпадают'}, status=status.HTTP_400_BAD_REQUEST)

        user.nickname = new_nickname
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
            data=(token_serializer_class(token).data, ({"nickname": serializer.user.nickname}),
                  ({"email": serializer.user.email}), ({"is_superuser": serializer.user.is_superuser}),
                  ({"id": serializer.user.id}), ({"password": serializer.user.password})),
            status=status.HTTP_200_OK,
        )

    @login_user
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TokenDestroyViewApi(TokenDestroyView):
    permission_classes = settings.PERMISSIONS.token_destroy

    @logout_user
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

    @article_get_all
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @article_post
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ArticleAPIUpdateView(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)

    def perform_update(self, serializer):
        serializer.save(date=datetime.date.today())

    @article_put
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @article_patch
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


class ArticleAPIDestroyView(generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)

    @article_delete
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class ArticleDetailView(APIView):

    @article_detail_get
    def get(self, request, pk):
        try:
            article = Article.objects.get(id=pk)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UsersDetailView(APIView):
    @get_user
    def get(self, request, pk):
        try:
            article = User.objects.get(id=pk)
            serializer = UserSerializer(article)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class TopicAPIList(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    @topic_get_all
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class TopicAPIAdd(generics.CreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (IsAdminOrReadOnly,)

    @topic_post
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TopicAPIDelete(generics.DestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (IsAdminOrReadOnly,)

    @topic_delete
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class TopicAPIUpdate(generics.UpdateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (IsAdminOrReadOnly,)

    @topic_put
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @topic_patch
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


class TopicDetailView(APIView):
    @topic_detail_get
    def get(self, request, pk):
        try:
            topic = Topic.objects.get(id=pk)
            serializer = TopicSerializer(topic)
            return Response(serializer.data)
        except Topic.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
