from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


def get_sentinel_user(*args):
    return get_user_model().objects.get_or_create(username=args[0])[0]


class News(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Название')
    description = models.CharField(max_length=1000, default='', verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(verbose_name='Количество просмотров', default=0)
    is_active = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))

    def __str__(self):
        return '{}. ({})'.format(self.title, self.created_at)


class Comment(models.Model):
    name_user = models.CharField(max_length=100, verbose_name='Имя и фамилия')
    text = models.CharField(max_length=1000, verbose_name='Текст')
    news = models.ForeignKey('News', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    USERNAME_FIELD = 'user'
    city = models.CharField(max_length=36, blank=True)
    phone = models.IntegerField(verbose_name='номер телефона', blank=True)
    is_verified = models.BooleanField(default=False)
    news_count = models.IntegerField(verbose_name='количество опубликованных новостей', default=0)

    def __str__(self):
        return str(self.user)