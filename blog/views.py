# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #достаем посты из БД, осторитированные по дате публикации
	return render(request, 'blog/post_list.html', {'posts': posts}) #собираем шаблон страницы постов, передаем ему список постов

def post_detail(request,pk):
	post = get_object_or_404(Post, pk=pk) #получаем пос по ключу или выводим 404
	return render(request, 'blog/post_detail.html', {'post': post}) #собираем ответ и шаблон