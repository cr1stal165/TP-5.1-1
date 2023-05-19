from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from reportlab.pdfgen import canvas
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from gtts import gTTS
from backend.models import Article


def index(request):
    return render(request, 'index.html')


def all_topics(request):
    return render(request, 'all_topics.html')


def article_page(request, pk):
    return render(request, 'article_page.html')


def login_page(request):
    return render(request, 'login.html')


def registration_page(request):
    return render(request, 'registration.html')


def profile_page(request):
    return render(request,'myprofile.html')


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

