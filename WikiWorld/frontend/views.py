from django.contrib.auth.decorators import login_required
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from gtts import gTTS
from rest_framework.permissions import IsAuthenticated

from backend.models import Article


def index(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return redirect('index_auth')
    else:
        return render(request, 'index.html')


def all_topics(request):
    if request.user.is_authenticated:
        return redirect('all_topics_auth')
    else:
        return render(request, 'all_topics.html')


def article_page(request, pk):
    return render(request, 'article_page.html')


def articles_topic(request, pk):
    return render(request, 'articles_topic.html')


def login_page(request):
    return render(request, 'login.html')


def registration_page(request):
    return render(request, 'registration.html')


def profile_page(request):
    return render(request, 'auth_template/myprofile.html')


def index_auth(request):
    return render(request, 'auth_template/main_authorised.html')


def edit_profile_auth(request):
    return render(request, 'auth_template/editprofile.html')


def article_page_auth(request, pk):
    return render(request, 'auth_template/article_page_auth.html')


def articles_topic_auth(request, pk):
    return render(request, 'auth_template/articles_topic_auth.html')


def all_topics_auth(request):
    return render(request, 'auth_template/all_topics_auth.html')


def add_article(request):
    return render(request, 'auth_template/add_article.html')


def edit_article(request):
    return render(request, 'auth_template/edit_article.html')


def admin_thematics(request):
    return render(request, 'admin_template/admin_thematics.html')


def admin_many_articles(request):
    return render(request, 'admin_template/admin_many_articles.html')


def admin_edit_article(request):
    return render(request, 'admin_template/admin_edit_article.html')


def admin_edit_thematics(request):
    return render(request, 'admin_template/admin_edit_thematics.html')


def download_pdf(request):
    global pdf
    if request.method == 'POST':
        art_id = request.POST.get('hid_id')
        descript = Article.objects.get(id=art_id)
        # # Установка шрифта и кодировки
        pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf', 'Windows-1251'))
        pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
        pdfmetrics.registerFont(TTFont('Arial-Bold', 'arialbd.ttf', 'Windows-1251'))
        pdfmetrics.registerFont(TTFont('Arial-Italic', 'ariali.ttf', 'Windows-1251'))
        pdfmetrics.registerFont(TTFont('Arial-BoldItalic', 'arialbi.ttf', 'Windows-1251'))
        # Создание нового документа PDF
        pdf = canvas.Canvas("example.pdf", pagesize=A4, )

        # Добавление текста в документ
        text = descript.description
        pdf.setFont('Arial', 12)
        pdf.drawString(100, 100, text)

        # Сохранение документа
        pdf.save()

        # Открытие файла PDF и чтение его содержимого
        with open("example.pdf", "rb") as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type="application/pdf")
            response["Content-Disposition"] = 'attachment; filename="example.pdf"'
            return response


def download_audio(request):
    if request.method == 'POST':
        art_id = request.POST.get('hid_id1')
        descript = Article.objects.get(id=art_id)

        text = descript.description
        language = 'ru'

        # создание объекта gTTS
        tts = gTTS(text=text, lang=language)

        # сохранение аудиофайла
        tts.save("audio.mp3")

        with open("audio.mp3", "rb") as file:
            response = HttpResponse(file.read(), content_type="audio/mpeg")
            response["Content-Disposition"] = 'attachment; filename=audio.mp3'
            return response
