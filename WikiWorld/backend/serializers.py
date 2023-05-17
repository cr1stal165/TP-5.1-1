from rest_framework import serializers

from backend.models import Article, User, Topic


class ArticleSerializer(serializers.ModelSerializer):
    date = serializers.DateField(read_only=True)
    user = serializers.CurrentUserDefault()

    class Meta:
        model = Article
        fields = "__all__"


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('nickname',)


