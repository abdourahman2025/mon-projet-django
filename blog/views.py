from django.shortcuts import render
from .models import Article

def accueil(request):
    articles = Article.objects.all()
    return render(request, 'blog/accueil.html', {'articles': articles})