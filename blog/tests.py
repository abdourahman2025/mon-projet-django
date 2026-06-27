from django.test import TestCase, Client
from django.urls import reverse
from .models import Article

class TestPages(TestCase):

    def setUp(self):
        self.client = Client()
        Article.objects.create(
            titre="Mon premier article",
            contenu="Contenu de test pour cet article."
        )

    def test_page_accueil_retourne_200(self):
        """La page d'accueil doit retourner 200"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_page_accueil_contient_article(self):
        """La page doit afficher le titre de l'article"""
        response = self.client.get('/')
        self.assertContains(response, "Mon premier article")

    def test_page_inexistante_retourne_404(self):
        """Une URL inconnue doit retourner 404"""
        response = self.client.get('/page-inexistante/')
        self.assertEqual(response.status_code, 404)


class TestModeleArticle(TestCase):

    def test_creation_article(self):
        """Un article doit être créé correctement"""
        article = Article.objects.create(
            titre="Test titre",
            contenu="Test contenu"
        )
        self.assertEqual(article.titre, "Test titre")
        self.assertEqual(str(article), "Test titre")