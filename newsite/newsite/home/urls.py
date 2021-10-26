from django.urls import path
from .views import AddPostView, HomeView, ArticleDetailView, UpdateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/', AddPostView.as_view(), name='add_post'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/edit/<int:pk>/', UpdateView.as_view(), name='update-article')

]
