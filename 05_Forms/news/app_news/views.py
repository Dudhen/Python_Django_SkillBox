from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import News, get_sentinel_user, Profile
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from .forms import CommentForm, CommentForm2, RegisterUserForm, RegisterProfileForm, NewsActiveForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView


class NewsListView(generic.ListView):
    model = News
    template_name = 'news/news_list.html'
    users_in_group_verif = Group.objects.get(name="Верифицированные пользователи")#.user_set.all()
    users_in_group_moder = Group.objects.get(name="Модераторы")#.user_set.all()
    users_in_group_simple = Group.objects.get(name="Обычные пользователи")

    def get_context_data(self, **kwargs):
        if self.request.user.profile.is_verified:
            if not self.request.user.groups.filter(name='Верифицированные пользователи'):
                if not self.request.user.groups.filter(name='Модераторы'):
                    self.request.user.groups.add(self.users_in_group_verif)
                    self.request.user.groups.remove(self.users_in_group_simple)
                else:
                    self.request.user.groups.add(self.users_in_group_verif)
        else:
            if not self.request.user.groups.filter(name='Обычные пользователи'):
                if not self.request.user.groups.filter(name='Модераторы'):
                    self.request.user.groups.remove(self.users_in_group_verif)
                    self.request.user.groups.add(self.users_in_group_simple)
                else:
                    self.request.user.groups.remove(self.users_in_group_verif)
        context = super(NewsListView, self).get_context_data(**kwargs)
        if self.request.user.groups.filter(name='Верифицированные пользователи').exists():
            context['verifications_check'] = True
        if self.request.user.groups.filter(name='Модераторы'):
            context['moderators_check'] = True
        return context


class NewsDetailView(generic.DetailView):
    model = News
    template_name = 'news/news_detail.html'
    comment_form = CommentForm
    comment_form_2 = CommentForm2
    users_in_group = Group.objects.get(name="Модераторы").user_set.all()

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['datas'] = self.object.comments.all()
        if self.request.user.is_authenticated:
            context['comment_form'] = self.comment_form
        else:
            context['comment_form'] = self.comment_form_2
        if self.request.user in self.users_in_group:
            context['moderators_check'] = True
        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            news = self.get_object()
            if self.request.user.is_authenticated:
                comment = comment_form.save(commit=False)
                user = get_sentinel_user(request.user.username)
                name_user = user.username
                comment.user = user
                comment.news = news
                comment.name_user = name_user
                comment.save()
            else:
                comment = comment_form.save(commit=False)
                anonim_username = self.request.POST.get('name_user') + ' (Аноним)'
                user = get_sentinel_user(anonim_username)
                comment.user = user
                comment.news = news
                comment.name_user = anonim_username
                comment.save()
            return HttpResponseRedirect('/news/{}/'.format(news.id))
        return render(request, 'news/news_detail.html', context={'comment_form': comment_form,
                                                                 'datas': self.object.comments.all()})


class NewsFormView(CreateView):
    model = News
    fields = ['title', 'description']
    template_name = 'news/new_news.html'
    success_url = '/news/'

    def form_valid(self, form):
        self.request.user.profile.news_count += 1
        return super().form_valid(form)


class NewsEditFormView(UpdateView):
    model = News
    fields = ['title', 'description']
    template_name = 'news/news_edit.html'
    success_url = '/news/'


class UserLoginView(LoginView):
    template_name = 'news/login.html'


class UserLogout(LogoutView):
    next_page = '/login/'


class UserRegister(CreateView):
    form_class = RegisterUserForm
    form_class_2 = RegisterProfileForm
    template_name = 'news/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super(UserRegister, self).get_context_data(**kwargs)
        context['user_form'] = self.form_class
        context['profile_form'] = self.form_class_2
        return context

    def post(self, request, *args, **kwargs):
        user_form = RegisterUserForm(request.POST)
        profile_form = RegisterProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            profile = profile_form.save(commit=False)
            user.save()
            profile.user = user
            profile.save()
            user_group = Group.objects.get(name='Обычные пользователи')
            user.groups.add(user_group)
            return redirect('login')
        else:
            return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})


class PersonalInfoDetailView(generic.ListView):
    model = Profile
    template_name = 'news/profile_list.html'


class PersonalInfoEditFormView(UpdateView):
    model = Profile
    fields = ['city', 'phone']
    template_name = 'news/profile_edit.html'
    success_url = '/profile/'


class UsersListView(generic.ListView):
    models = Profile
    template_name = 'news/users_list.html'

    def get_queryset(self):
        return Profile.objects.order_by('id')


class PersonalVerificationEditFormView(UpdateView):
    model = Profile
    fields = ['is_verified']
    template_name = 'news/users_edit.html'
    success_url = '/users/'


class NewsNotActiveListView(generic.ListView):
    model = News
    template_name = 'news/news_not_active_list.html'
    fields = ['is_active']
    form_class = NewsActiveForm

    def get_context_data(self, **kwargs):
        context = super(NewsNotActiveListView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        try:
            news_list = News.objects.get(is_active=False)
        except self.model.DoesNotExist:
            news_list = False
        context['objects_do_not_active'] = news_list
        return context


class NewsNotActiveEditFormView(UpdateView):

    model = News
    fields = ['is_active']
    template_name = 'news/news_not_active_edit.html'
    success_url = '/not-active-news/'
