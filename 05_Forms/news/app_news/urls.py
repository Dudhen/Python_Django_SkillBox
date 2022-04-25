from .import views
from django.urls import path
from .views import NewsFormView, NewsEditFormView, UserLoginView, UserLogout, UserRegister, \
    PersonalInfoDetailView, PersonalInfoEditFormView, UsersListView, PersonalVerificationEditFormView, \
    NewsNotActiveListView, NewsNotActiveEditFormView

urlpatterns = [
    path(r'news/', views.NewsListView.as_view(), name='news'),
    path(r'news/<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path(r'news/new_news/', NewsFormView.as_view()),
    path(r'news/<int:pk>/edit/', NewsEditFormView.as_view()),
    path(r'login/', UserLoginView.as_view(), name='login'),
    path(r'logout/', UserLogout.as_view(), name='logout'),
    path(r'registrations/', UserRegister.as_view(), name='registrations'),
    path(r'profile/', PersonalInfoDetailView.as_view(), name='profile'),
    path(r'profile/<int:pk>/edit/', PersonalInfoEditFormView.as_view()),
    path(r'users/', UsersListView.as_view(), name='users'),
    path(r'profile/<int:pk>/edit_verification/', PersonalVerificationEditFormView.as_view(), name='users'),
    path(r'not-active-news/', NewsNotActiveListView.as_view(), name='news-not-active'),
    path(r'not-active-news/<int:pk>/edit/', NewsNotActiveEditFormView.as_view()),
]