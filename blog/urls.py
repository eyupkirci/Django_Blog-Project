from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
    home, 
    about, 
    # login, 
    register, 
    postadd, 
    profile, 
    profileupdate, 
    profileadd,
    like,
    postupdate,
    postdelete,
    postdetail,
    )

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('register', register, name='register'),

    # auth_views (login, logout)
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    # profile
    path('profile', profile, name='profile'),
    path('profileadd', profileadd, name='profileadd'),
    path('profileupdate', profileupdate, name='profileupdate'),

    # post
    path('postadd', postadd, name='postadd'),
    path('postupdate/<int:id>', postupdate, name='postupdate'),
    path('postdelete/<int:id>', postdelete, name='postdelete'),
    path('postdetail/<str:slug>', postdetail, name='postdetail'),


    # actions
    path('like/<int:id>', like, name='like'),
]