from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from app.models import Article
from django.views.generic import CreateView


def home(request):
    articles = Article.objects.all()
    return render(request, "app/home.html", {"articles": articles})


class CreateArticleView(CreateView):
    model = Article
    fields = ["title", "content", "word_count", "twitter_post", "status"]
    template_name = "app/article_create.html"
    success_url = reverse_lazy("home")
