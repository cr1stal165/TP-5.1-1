from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from backend.models import Topic, User, Article
from backend.serializers import TopicSerializer, ArticleSerializer


class TopicAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        Topic.objects.create(name='Topic1', image='byte_string1')
        Topic.objects.create(name='Topic2', image='byte_string2')

    def test_get_topic_list(self):
        url = reverse('topics')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data[0]['name'], 'Topic1')
        self.assertEqual(response.data[0]['image'], 'byte_string1')
        self.assertEqual(response.data[1]['name'], 'Topic2')
        self.assertEqual(response.data[1]['image'], 'byte_string2')


class TopicDetailViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.topic = Topic.objects.create(name="Test Topic", image='byte string')

    def test_get_existing_topic(self):
        url = reverse('topic-detail', kwargs={'pk': self.topic.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = TopicSerializer(self.topic)
        self.assertEqual(response.data, serializer.data)

    def test_get_nonexistent_topic(self):
        url = reverse('topic-detail', kwargs={'pk': 999})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TopicAPIAddTestAdmin(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(nickname='exampleUser', password='example1', email='example@mail.ru')
        self.token = self.get_token()

    def get_token(self):
        url = reverse('login')
        data = {'nickname': 'exampleUser', 'password': 'example1', 'email': 'example@mail.ru'}
        response = self.client.post(url, data, format='json')
        return response.data[0]

    def test_create_topic_authenticated_user(self):
        url = reverse('topic-add')
        data = {'name': 'Test Topic12', 'image': 'byte_string'}
        headers = {'Authorization': f'Bearer {self.token}'}
        response = self.client.post(url, data, format='json', headers=headers)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        topic = Topic.objects.get()
        self.assertEqual(topic.name, 'Test Topic12')


class TopicAPIAddTestUnauthorized(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_topic_unauthenticated_user(self):
        url = reverse('topic-add')
        data = {'name': 'Test Topic', 'image': 'byte_string'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TopicAPIUpdateTestUnauthorized(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_update_topic_admin(self):
        self.topic = Topic.objects.create(name='Test Topic', image='byte_string')

        url = reverse('topic-update', args=[self.topic.id])
        data = {'name': 'Updated Topic', 'image': 'byte_string'}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TopicAPIDeleteTestUnauthorized(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_delete_topic_unauthorized(self):
        topic = Topic.objects.create(name='Test Topic', image='byte_string')

        url = reverse('topic-delete', args=[topic.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertTrue(Topic.objects.filter(pk=topic.pk).exists())


class ArticleAPIListGetTest(APITestCase):
    def setUp(self):
        self.url = reverse('article-get-post')

    def test_get_articles(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ArticleAPIListCreateTest(APITestCase):
    def setUp(self):
        self.url = reverse('article-get-post')
        self.user = User.objects.create_user(nickname='exampleUser', password='example1', email='example@mail.ru')
        self.token = self.get_token()

    def get_token(self):
        url = reverse('login')
        data = {'nickname': 'exampleUser', 'password': 'example1', 'email': 'example@mail.ru'}
        response = self.client.post(url, data, format='json')
        return response.data[0]

    def test_create_article_authenticated_user(self):
        topic = Topic.objects.create(name='Test Topic', image='byte_string')

        url = reverse('article-get-post')
        data = {
            'title': 'Test Article',
            'description': 'Test description',
            'image': 'byte_string',
            'user': self.user.id,
            'topic': topic.id
        }
        headers = {'Authorization': f'Bearer {self.token}'}
        response = self.client.post(url, data, format='json', headers=headers)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ArticleAPIListUpdateUnauthorizedTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(nickname='exampleUser', password='example1', email='example@mail.ru')
        self.topic = Topic.objects.create(name='Test Topic', image='byte_string')
        self.article = Article.objects.create(title='Test Article', description='Test description', image='byte_string',
                                              topic_id=self.topic.id, user_id=self.user.id, date='2023-09-09')

    def test_update_article_unauthorized_user(self):
        url = reverse('article-update', args=[self.article.id])
        data = {'title': 'Updated Article', 'description': 'Updated description', 'image': 'byte_string'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ArticleAPIDestroyTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(nickname='testuser', password='testpassword', email='testmail.ru')
        self.topic = Topic.objects.create(name='Topic123', image='byte_string')
        self.article = Article.objects.create(title='Test Article', description='Test description', image='byte_string'
                                              , date='2023-09-02', user_id=self.user.id, topic_id=self.topic.id)
        self.url = reverse('article-delete', args=[self.article.pk])
        self.client.force_authenticate(user=self.user)

    def test_delete_article_authorized_user(self):
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Article.objects.filter(pk=self.article.pk).exists())

    def test_delete_article_unauthorized_user(self):
        self.client.logout()
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertTrue(Article.objects.filter(pk=self.article.pk).exists())


class ArticleDetailViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(nickname='testuser', password='testpassword', email='testmail.ru')
        self.topic = Topic.objects.create(name='Topic123', image='byte_string')
        self.article = Article.objects.create(title='Test Article', description='Test description',
                                              image='byte_string', date='2023-09-09', user_id=self.user.id,
                                              topic_id=self.topic.id)
        self.url = reverse('article-detail', args=[self.article.pk])

    def test_get_existing_article(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, ArticleSerializer(self.article).data)

    def test_get_nonexistent_article(self):
        invalid_url = reverse('article-detail', args=[999])
        response = self.client.get(invalid_url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UserDetailViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(nickname='testuser', password='testpassword', email='testmail.ru')
        self.url = reverse('user', args=[self.user.id])

    def test_get_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_nonexistent_user(self):
        invalid_url = reverse('user', args=[99999999])
        response = self.client.get(invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class RegistrUserViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('registration')

    def test_register_user(self):
        data = {
            'nickname': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com'
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['response'])
        self.assertEqual(User.objects.count(), 1)

        user = User.objects.get(nickname='testuser')
        self.assertEqual(user.nickname, 'testuser')
        self.assertEqual(user.email, 'test@example.com')


class TokenDestroyViewApiTest(APITestCase):
    def setUp(self):
        self.url = reverse('logout')
        self.user = User.objects.create_user(nickname='testuser', password='testpassword', email='testmail@com.com')
        self.client.login(nickname='testuser', password='testpassword', email='testmail@com.com')

    def test_logout_user(self):
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(self.client.session.has_key('_auth_user_id'))


class UpdatePasswordUserViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(nickname='testuser', password='testpassword', email='testmail@mail.com')
        self.url = reverse('update-user')
        self.client.login(nickname='testuser', password='testpassword', email='testmail@mail.com')

    def test_update_password(self):
        data = {
            'password': 'newpassword',
            'nickname': 'newnickname'
        }

        response = self.client.put(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('newpassword'))
        self.assertEqual(self.user.nickname, 'newnickname')
