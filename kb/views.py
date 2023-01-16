from django.shortcuts import render
from .models import Article

# Create your views here.


def home(request):
    # return HttpResponse('<h1>Knowledge base - homepage</h1>')
    # articles = [
    #     {
    #         'author': 'John Doe',
    #         'title': 'How to start development server',
    #         'content': 'python manage.py runserver',
    #         'date': 'December 4, 2021'
    #     },
    #     {
    #         'author': 'Max Doe',
    #         'title': 'How to stop the development server',
    #         'content': 'Ctrl-C',
    #         'date': 'December 4, 2021'
    #     }

    # ]
    context = {'title': 'Articles', 'articles': Article.objects.all()}
    return render(request, 'kb/home.html', context)


def about(request):
    # return HttpResponse('<h1> About knowledge base</h1>')
    context = {'title': 'About KB'}
    return render(request, 'kb/about.html', context)
