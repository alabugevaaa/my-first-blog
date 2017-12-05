# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class Post(models.Model): #определяем объект "пост"
    author = models.ForeignKey('auth.User') #определяем свойства объекта
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): #метод публикации
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self): #метод возвращает заголовок
        return self.title
