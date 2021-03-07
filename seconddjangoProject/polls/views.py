from django.shortcuts import render

# Create your views here.
from polls.models import Article
from .owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class ArticleListView(OwnerListView):
    model = Article
    # By convention:
    # template_name = "myarts/article_list.html"


class ArticleDetailView(OwnerDetailView):
    model = Article


class ArticleCreateView(OwnerCreateView):
    model = Article
    fields = ['title', 'text']


class ArticleUpdateView(OwnerUpdateView):
    model = Article
    fields = ['title', 'text']


class ArticleDeleteView(OwnerDeleteView):
    model = Article
