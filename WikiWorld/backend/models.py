from django.db import models


class User(models.Model):
    nickname = models.CharField(max_length=100)
    email = models.CharField()
    password = models.CharField(max_length=24)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.nickname


class Topic(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image_topic')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField()
    date = models.DateField()
    image = models.ImageField(upload_to='photos')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " " + f'{self.date}'
