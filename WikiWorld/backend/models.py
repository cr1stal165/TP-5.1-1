from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class MyUserManager(BaseUserManager):

    def _create_user(self, nickname, email, password, **extra_fields):
        if len(password) < 8:
            raise ValueError('Минимальная длина пароля 8 символов')
        elif len(nickname) < 4:
            raise ValueError('Минимальная длина никнейма 4 символов')

        user = User(
            nickname=nickname,
            email=email,
            **extra_fields
        )

        user.set_password(password)
        user.save()
        return user


    def create_user(self, nickname, email, password):
        return self._create_user(nickname,email,password)


    def create_superuser(self, nickname, email, password):
        return self._create_user(nickname,email,password, is_staff=True, is_superuser=True)



class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    nickname = models.CharField(max_length=100, unique=True)
    email = models.CharField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'nickname'

    objects = MyUserManager()

    def __str__(self):
        return self.nickname


class Topic(models.Model):
    name = models.CharField(max_length=100)
    image = models.BinaryField(null=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField()
    date = models.DateField()
    image = models.BinaryField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)


# class Token(models.Model):
#     key = models.CharField(max_length=40, primary_key=True)
#     user = models.ForeignKey('auth.User', related_name='auth_tokens', on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         db_table = 'authtoken_token'