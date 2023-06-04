from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render, redirect
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from django.shortcuts import get_object_or_404
from gtts import gTTS
from backend.models import Article


def index(request):
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
    global temp
    temp = pk
    if request.user.is_authenticated:
        return redirect('article_page_auth', pk=pk)
    else:
        return render(request, 'article_page.html')


def articles_topic(request, pk):
    if request.user.is_authenticated:
        return redirect('articles_topic_auth', pk=pk)
    else:
        return render(request, 'articles_topic.html')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('profile_page')
    else:
        return render(request, 'login.html')


def registration_page(request):
    if request.user.is_authenticated:
        return redirect('profile_page')
    else:
        return render(request, 'registration.html')


def profile_page(request):
    if not request.user.is_authenticated:
        return redirect('index')
    return render(request, 'auth_template/myprofile.html')


def index_auth(request):
    if request.user.is_superuser:
        return redirect('admin_main')
    if not request.user.is_authenticated:
        return redirect('index')
    return render(request, 'auth_template/main_authorised.html')


def edit_profile_auth(request):
    if request.user.is_superuser:
        return redirect('admin_main')
    if not request.user.is_authenticated:
        return redirect('index')
    return render(request, 'auth_template/editprofile.html')


def article_page_auth(request, pk):
    if request.user.is_superuser:
        return redirect('admin_main')
    if not request.user.is_authenticated:
        return redirect('article_page', pk=pk)
    return render(request, 'auth_template/article_page_auth.html')


def articles_topic_auth(request, pk):
    if request.user.is_superuser:
        return redirect('admin_main')
    if not request.user.is_authenticated:
        return redirect('articles_topic', pk=pk)
    return render(request, 'auth_template/articles_topic_auth.html')


def all_topics_auth(request):
    if request.user.is_superuser:
        return redirect('admin_main')
    if not request.user.is_authenticated:
        return redirect('all_topics')
    return render(request, 'auth_template/all_topics_auth.html')


def add_article(request):
    if request.user.is_superuser:
        return redirect('admin_main')
    if not request.user.is_authenticated:
        return redirect('index')
    return render(request, 'auth_template/add_article.html')


def edit_article(request, pk):
    if request.user.is_superuser:
        return redirect('admin_main')
    if not request.user.is_authenticated:
        return redirect('index')
    return render(request, 'auth_template/edit_article.html')


def admin_main(request):
    if request.user.is_superuser:
        return render(request, 'admin_template/adminmain.html')
    elif request.user.is_authenticated and not request.user.is_authenticated:
        return redirect('index_auth')
    else:
        return redirect('index')


def admin_thematics(request):
    if request.user.is_superuser:
        return render(request, 'admin_template/admin_thematics.html')
    elif request.user.is_authenticated and not request.user.is_authenticated:
        return redirect('index_auth')
    else:
        return redirect('index')


def admin_many_articles(request):
    if request.user.is_superuser:
        return render(request, 'admin_template/admin_many_articles.html')
    elif request.user.is_authenticated and not request.user.is_authenticated:
        return redirect('index_auth')
    else:
        return redirect('index')


def admin_edit_article(request, pk):
    if request.user.is_superuser:
        return render(request, 'admin_template/admin_edit_article.html')
    elif request.user.is_authenticated and not request.user.is_authenticated:
        return redirect('index_auth')
    else:
        return redirect('index')


def admin_edit_thematics(request, pk):
    if request.user.is_superuser:
        return render(request, 'admin_template/admin_edit_thematics.html')
    elif request.user.is_authenticated and not request.user.is_authenticated:
        return redirect('index_auth')
    else:
        return redirect('index')


def admin_add_thematics(request):
    if request.user.is_superuser:
        return render(request, 'admin_template/admin_add_thematis.html')
    elif request.user.is_authenticated and not request.user.is_authenticated:
        return redirect('index_auth')
    else:
        return redirect('index')


def page_not_found(request, exception):
    return render(request, 'page_not_found.html', status=404)


def download_pdf(request):
    if request.method == 'POST':
        art_id = request.POST.get('hid_id')
        descript = get_object_or_404(Article, id=art_id)

        # Set up the document with A4 size
        pdf_buffer = BytesIO()
        pdf = SimpleDocTemplate(pdf_buffer, pagesize=A4, encoding='utf-8')
        styles = getSampleStyleSheet()

        font_path = 'frontend/static/fonts/Montserrat-Regular.ttf'
        pdfmetrics.registerFont(TTFont('Montserrat', font_path))
        font_path1 = 'frontend/static/fonts/Montserrat-Bold.ttf'
        pdfmetrics.registerFont(TTFont('Montserrat-Bold', font_path1))


        # Add the article title to the document
        title_style = ParagraphStyle(
            'TitleStyle',
            parent=styles['Heading1'],
            fontSize=16,
            leading=18,
            spaceAfter=12,
            fontName='Montserrat-Bold',  # Specify the registered font name
            alignment=1,  # Center alignment
            fontWeight='bold',  # Make the title bold
            language='en',
        )
        title_paragraph = Paragraph(descript.title, title_style)

        # Add the article text to the document
        text = descript.description
        article_style = ParagraphStyle(
            'ArticleStyle',
            parent=styles['Normal'],
            fontSize=12,
            leading=14,
            spaceAfter=12,
            fontName='Montserrat',  # Specify the registered font name
            language='en',
        )
        article_paragraphs = [Paragraph(line, article_style) for line in text.split('\n')]

        # Build the document content
        content = [title_paragraph] + article_paragraphs

        # Build the PDF document
        pdf.build(content)

        # Get the PDF file from the buffer
        pdf_buffer.seek(0)
        response = HttpResponse(
            pdf_buffer.read(),
            content_type='application/pdf'
        )
        response['Content-Disposition'] = 'attachment; filename="example.pdf"'
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
        tts.save("frontend/static/audio.mp3")

        with open("frontend/static/audio.mp3", "rb") as file:
            response = HttpResponse(file.read(), content_type="audio/mpeg")
            response["Content-Disposition"] = 'attachment; filename=audio.mp3'
            return response


def play_music(request):
    if request.method == 'POST':
        art_id = request.POST.get('hid_id2')
        descript = Article.objects.get(id=art_id)

        text = descript.description
        language = 'ru'

        # создание объекта gTTS
        tts = gTTS(text=text, lang=language)

        # сохранение аудиофайла
        tts.save("frontend/static/audio.mp3")
        return redirect('article_page', pk=temp)
