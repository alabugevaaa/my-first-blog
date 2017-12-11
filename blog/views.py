# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #достаем посты из БД, осторитированные по дате публикации
	return render(request, 'blog/post_list.html', {'posts': posts}) #собираем шаблон страницы постов, передаем ему список постов

def post_detail(request,pk):
	post = get_object_or_404(Post, pk=pk) #получаем пост по ключу или выводим 404
	return render(request, 'blog/post_detail.html', {'post': post}) #собираем ответ и шаблон

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST) #передаем форме данные
		if form.is_valid(): #если форма валидна
			post = form.save(commit=False) #пока не сохраняем форму
			post.author = request.user #добаляем автора
			post.published_date = timezone.now() #добаляем дату публикации
			post.save() #сохраням форму
			return redirect('post_detail', pk=post.pk) #отправляем на страницу поста
	else:
		form = PostForm() #создаем пустую форму

	return render(request, 'blog/post_edit.html', {'form': form}) #собираем страницу с формой

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post) #передаем форме экземпляр объекта пост
		if form.is_valid(): #если форма валидна
			post = form.save(commit=False) #пока не сохраняем форму
			post.author = request.user #добаляем автора
			post.published_date = timezone.now() #добаляем дату публикации
			post.save() #сохраням форму
			return redirect('post_detail', pk=post.pk) #отправляем на страницу поста
	else:
		form = PostForm(instance=post) #создаем форму с экземпляром объекта

	return render(request, 'blog/post_edit.html', {'form': form})

def sqrt(request):
	return render(request, 'blog/sqrt.html')