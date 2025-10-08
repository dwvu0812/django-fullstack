from django.shortcuts import render, redirect
from app.forms import CreateArticleForm
from app.models import Article


def home(request):
    articles = Article.objects.all()
    return render(request, "app/home.html", {"articles": articles})


def create_article(request):
    if request.method == "POST":
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            new_article = Article.objects.create(
                title=form_data["title"],
                content=form_data["content"],
                word_count=form_data["word_count"],
                twitter_post=form_data["twitter_post"],
                status=form_data["status"],
            )
            new_article.save()
            return redirect("home")
    else:
        form = CreateArticleForm()
    return render(request, "app/article_create.html", {"form": form})
