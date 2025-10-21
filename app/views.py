from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from app.models import Article
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "app/home.html"
    context_object_name = "articles"

    def get_queryset(self):
        # Chỉ hiển thị articles của user hiện tại
        return Article.objects.filter(creator=self.request.user).order_by("-created_at")


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "app/article_create.html"
    model = Article
    fields = ["title", "content", "twitter_post", "status"]
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "app/article_update.html"
    model = Article
    fields = ["title", "content", "twitter_post", "status"]
    success_url = reverse_lazy("home")

    def get_queryset(self):
        # Chỉ cho phép user edit articles của chính họ
        return Article.objects.filter(creator=self.request.user)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = "app/article_delete.html"
    success_url = reverse_lazy("home")

    def get_queryset(self):
        # Chỉ cho phép user xóa articles của chính họ
        return Article.objects.filter(creator=self.request.user)
