from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/profile_update/', views.profile_update, name="profile-update"),
    path('save_news/<int:news_id>/', views.save_news, name='save_news'),
    path('remove_news/<int:news_id>/', views.remove_news, name='remove_news'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
]