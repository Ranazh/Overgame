from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from taggit.models import Tag

from post import models, forms
from django.urls import reverse_lazy

# Create your views here.
from .models import Post


class PostCreateView(generic.CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'post/postcreate.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.instance.author = self.request.user.userprofile
        form.save(commit=True)
        return super(PostCreateView, self).form_valid(form)


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/main.html', {'posts': posts})


def post_by_tag(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    posts = Post.objects.filter(tags__name=tag)
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'post/postlist.html', context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    if post.favourite.filter(id=request.user.id).exists():
        is_favorite = True
    else:
        is_favorite = False

    return render(request, 'post/postbase.html', {'post': post})


def post_favourite(request, pk):
    post = Post.objects.get(pk=pk)
    if post.favourite.filter(pk=request.user.id).exists():
        is_favorite = True
        post.favourite.remove(request.user)
    else:
        is_favorite = False
        post.favourite.add(request.user)

    return render(request, 'post:detail', {'post': post})

'''
            if request.method == 'POST':
        favourite = post
        user = request.user
        user.favorites.add(favourite)
        if post.favourite.filter(id=request.user.id).exists():
            is_favorite = True
            post.favourite.remove(request.user)
        else:
            is_favorite = False
            post.favourite.add(request.user)
        '''

"""
class PostDetailView(generic.DeleteView):
    model = models.Post
    context_object_name = 'post'
    template_name = 'post/postbase.html'
    
class PostListView(generic.ListView):
    model = models.Post
    context_object_name = 'posts'
    template_name = 'post/postlist.html'
"""
