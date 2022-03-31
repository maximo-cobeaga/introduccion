from dataclasses import field
from multiprocessing import context
from re import template
from turtle import title
from django import views
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import View, UpdateView
from .forms import PostCreateForm
from .models import Post
from django.urls import reverse_lazy


class BlogListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context={   
            'posts': posts
        }
        return render(request, 'blog_list.html', context)


class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form=PostCreateForm()
        context={
            'form':form
        }
        return render(request, 'blog_create.html', context)

    def post(self, request, *args, **kwargs):
        if request.method=='POST':
            form = PostCreateForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data.get('title')
                content=form.cleaned_data.get('content')

                p, created = Post.objects.get_or_create(title=title, content=content)
                p.save()
                return redirect('blog:home')
        context={
            
        }
        return render(request, 'blog_create.html', context)

class BlogDatailView(View):
    def get(self, request, pk,*args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        context={
           'post':post 
        }
        return render(request, 'blog_detail.html', context)

class BlogUpdateView(UpdateView):
    model=Post
    fields=['title','content']
    template_name='blog_update.html'

    def get_succes_url(self): 
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detail', kwargs = {'pk':pk} )
