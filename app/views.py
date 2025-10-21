from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from app.models import Article
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import gettext as _


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "app/home.html"
    context_object_name = "articles"

    def get_queryset(self):
        # Only show articles of the current user
        return Article.objects.filter(creator=self.request.user).order_by("-created_at")


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "app/article_create.html"
    model = Article
    fields = ["title", "content", "twitter_post", "status"]
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        messages.success(self.request, _("Article created successfully!"))
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "app/article_update.html"
    model = Article
    fields = ["title", "content", "twitter_post", "status"]
    success_url = reverse_lazy("home")

    def get_queryset(self):
        # Only allow user to edit their own articles
        return Article.objects.filter(creator=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, _("Article updated successfully!"))
        return super().form_valid(form)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = "app/article_delete.html"
    success_url = reverse_lazy("home")

    def get_queryset(self):
        # Only allow user to delete their own articles
        return Article.objects.filter(creator=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _("Article deleted successfully!"))
        return super().delete(request, *args, **kwargs)
