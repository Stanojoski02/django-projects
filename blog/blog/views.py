from django.shortcuts import render
from datetime import date
from .models import Post, Author, Tag


def get_date(post):
    return post['date']


def starting_page(request):
    all_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, "blog/index.html", {"posts": all_posts})


def posts(requests):
    all_posts = Post.objects.all().order_by('-date')
    return render(requests, 'blog/all-posts.html', {"posts": all_posts})


all_posts = []


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/post-detail.html', {'post': post})
