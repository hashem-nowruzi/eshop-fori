from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class Blog(ListView):
    model = Post
    paginate_by = 3

