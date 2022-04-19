from django.urls import path
from .views import index, about_me, login, register, editUser
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='index'),
    path('about_me', about_me, name='about_me'),
    path('login', login, name='login'),
    path('logout', LogoutView.as_view(template_name = 'index/logout.html'), name='logout'),
    path('register', register, name='register'),
    path('editUser', editUser, name='editUser')
]
