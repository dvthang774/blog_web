from django.db import models
from django.db.models import fields
from django.db.models.fields import PositiveBigIntegerField
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Entries
from django.http import HttpResponse
from .forms import PostForm

# Create your views here.
# def index(request):
#     return render(request, 'home/index.html')

class HomeView(ListView):
    model = Entries
    template_name = 'home/index.html'


    # def get_queryset(self):
    #     return Entries.objects.order_by('id')

class ArticleDetailView(DetailView):
    model = Entries
    template_name = 'home/article.html'
    context_object_name = 'post'


class AddPostView(CreateView):
    model = Entries
    form_class = PostForm
    template_name = 'home/add_post.html'
    # fields = '__all__'


class UpdateView(UpdateView):
    model = Entries
    template_name = 'home/update.html'
    fields = ['title', 'body']


 