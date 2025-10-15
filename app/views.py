from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from app.models import Article
from django.views.generic import CreateView, DeleteView, ListView, UpdateView


class ArticleListView(ListView):
    model = Article
    template_name = "app/home.html"
    context_object_name = "articles"


class ArticleCreateView(CreateView):
    template_name = "app/article_create.html"
    model = Article
    fields = ["title", "content", "twitter_post", "status"]
    success_url = reverse_lazy("home")


class ArticleUpdateView(UpdateView):
    template_name = "app/article_update.html"
    model = Article
    fields = ["title", "content", "twitter_post", "status"]
    success_url = reverse_lazy("home")


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "app/article_delete.html"
    success_url = reverse_lazy("home")
