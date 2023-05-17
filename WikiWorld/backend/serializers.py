from rest_framework import serializers
from .models import Article, User, Topic


class UserRegistrSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nickname', 'email', 'password']

    def save(self, *args, **kwargs):
        user = User(
            nickname=self.validated_data['nickname'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user


    def update(self, instance, validated_data):
        instance.password = validated_data.get('password', instance.password)
        return instance



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

