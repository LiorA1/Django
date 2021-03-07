from django.urls import path, reverse_lazy
from . import views

app_name='polls'
urlpatterns = [
    path('', views.ArticleListView.as_view(), name='all'),
    path('article/create', views.ArticleCreateView.as_view(success_url=reverse_lazy('polls:all')), name='article_create'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/update', views.ArticleUpdateView.as_view(success_url=reverse_lazy('polls:all')), name='article_update'),
    path('article/<int:pk>/delete', views.ArticleDeleteView.as_view(success_url=reverse_lazy('polls:all')), name='article_delete'),
]

# We use reverse_lazy in urls.py to delay looking up the view until all the paths are defined
