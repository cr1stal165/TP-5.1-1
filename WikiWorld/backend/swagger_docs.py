from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from backend.serializers import TopicSerializer, ArticleSerializer, UserSerializer

topic_detail_get = swagger_auto_schema(
    operation_summary='Get topic by id',
    tags=['Topics'],
    responses={
        200: openapi.Response(description='OK', schema=TopicSerializer),
        400: 'Bad Request',
        403: 'Forbidden',
        404: 'Not Found'
    }
)

topic_patch = swagger_auto_schema(
    operation_summary='Partial topic update',
    tags=['Topics'],
    responses={
        200: openapi.Response(description='OK', schema=TopicSerializer),
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found'
    }
)

topic_put = swagger_auto_schema(
    operation_summary='Update a topic',
    tags=['Topics'],
    responses={
        200: openapi.Response(description='OK', schema=TopicSerializer),
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found'
    }
)

topic_delete = swagger_auto_schema(
    operation_summary='Delete a topic',
    tags=['Topics'],
    responses={
        204: 'No Content',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed'
    }
)

topic_post = swagger_auto_schema(
    operation_summary='Create a new topic',
    tags=['Topics'],
    responses={
        201: openapi.Response(description='Created', schema=TopicSerializer),
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden'
    }
)

topic_get_all = swagger_auto_schema(
    operation_summary='Get all topics',
    tags=['Topics'],
    responses={
        200: openapi.Response(description='OK', schema=TopicSerializer),
        400: 'Bad Request',
        403: 'Forbidden',
        404: 'Not Found'
    }
)

article_get_all = swagger_auto_schema(
    operation_summary='Get all articles',
    tags=['Articles'],
    responses={
        200: openapi.Response(description='OK', schema=ArticleSerializer),
        400: 'Bad Request',
        403: 'Forbidden',
        404: 'Not Found'
    }
)

article_post = swagger_auto_schema(
    operation_summary='Create a new article',
    tags=['Articles'],
    responses={
        201: openapi.Response(description='Created', schema=ArticleSerializer),
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden'
    }
)

article_put = swagger_auto_schema(
    operation_summary='Update a article',
    tags=['Articles'],
    responses={
        200: openapi.Response(description='OK', schema=ArticleSerializer),
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found'
    }
)

article_patch = swagger_auto_schema(
    operation_summary='Partial article update',
    tags=['Articles'],
    responses={
        200: openapi.Response(description='OK', schema=ArticleSerializer),
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found'
    }
)

article_delete = swagger_auto_schema(
    operation_summary='Delete a article',
    tags=['Articles'],
    responses={
        204: 'No Content',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed'
    }
)

article_detail_get = swagger_auto_schema(
    operation_summary='Get article by id',
    tags=['Articles'],
    responses={
        200: openapi.Response(description='OK', schema=ArticleSerializer),
        400: 'Bad Request',
        403: 'Forbidden',
        404: 'Not Found'
    }
)

get_user = swagger_auto_schema(
    operation_summary='Get user',
    tags=['Users'],
    responses={
        200: openapi.Response(description='OK', schema=UserSerializer),
        400: 'Bad Request',
        403: 'Forbidden',
        404: 'Not Found'
    }
)

login_user = swagger_auto_schema(
    operation_summary='User authorization ',
    tags=['Users'],
    responses={
        200: openapi.Response(description='OK', schema=UserSerializer),
        400: 'Bad Request',
        403: 'Forbidden'
    }
)

logout_user = swagger_auto_schema(
    operation_summary='User logout',
    tags=['Users'],
    responses={
        200: openapi.Response(description='OK', schema=UserSerializer),
        400: 'Bad Request',
        403: 'Forbidden'
    }
)

registration_user = swagger_auto_schema(
    operation_summary='User registration',
    tags=['Users'],
    responses={
        200: openapi.Response(description='OK', schema=UserSerializer),
        400: 'Bad Request',
        403: 'Forbidden'
    }
)

update_password_put = swagger_auto_schema(
    operation_summary='User password update',
    tags=['Users'],
    responses={
        200: openapi.Response(description='OK', schema=UserSerializer),
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found'
    }
)

update_password_patch = swagger_auto_schema(
    operation_summary='Partial user password update',
    tags=['Users'],
    responses={
        200: openapi.Response(description='OK', schema=UserSerializer),
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found'
    }
)
