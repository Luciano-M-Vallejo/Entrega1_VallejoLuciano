from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from .models import Avatar
from .forms import CreationUser, EditUser


def index(request):
    return render(request, 'index/index.html', {})

def about_me(request):
    name = 'Luciano'
    lastName = 'Vallejo'
    course = 'Django + Python'
    
    dicc_data = {
        'name': name,
        'lastName': lastName,
        'course': course
    }
    return render(request, 'index/about_me.html', dicc_data)

def login(request):

    if  request.method == 'POST':
        formLogin = AuthenticationForm(request, data = request.POST)
        
        if formLogin.is_valid():
            username = formLogin.cleaned_data['username']
            password = formLogin.cleaned_data['password']
            
            user = authenticate(username = username, password = password)
            
            if user is not None:
                django_login(request, user)
                return render(request, 'index/index.html', {'msj': 'Bienvenido estas logueado!', 'loged': login_required})
            else:
                return render(request, 'index/login.html', {'formLogin': formLogin, 'msj': 'Este usuario no esta cargado'})
        else:
            return render(request, 'index/login.html', {'formLogin': formLogin, 'msj': 'Datos incorrectos'})
    else:
        formLogin = AuthenticationForm()
        return render(request, 'index/login.html', {'formLogin': formLogin})

def register(request):
    
    if request.method == 'POST':
        formCreationUser = CreationUser(request.POST)
        
        if formCreationUser.is_valid():
            username = formCreationUser.cleaned_data['username']
            formCreationUser.save()
            return render(request, 'index/index.html', {'msj': f'Se creo el usuario: {username}'})
        else:
            return render(request, 'index/register.html', {'formCreationUser': formCreationUser, 'msj': ''})
    
    formCreationUser = CreationUser()
    return render(request, 'index/register.html', {'formCreationUser': formCreationUser, 'msj': ''})

@login_required
def editUser(request):
    msj = ''
    if request.method == 'POST':
        formEditUser = EditUser(request.POST)
        
        if formEditUser.is_valid():
            
            data = formEditUser.cleaned_data          
            
            logued_user = request.user
            logued_user.email = data.get('email')
            logued_user.first_name = data.get('first_name', '')
            logued_user.last_name = data.get('last_name', '')
            if data.get('password1') == data.get('password2') and len(data.get('password1')) > 8:
                logued_user.set_password(data.get('password1'))
            else:
                msj = 'Error al modificar la contraseña'
            
            logued_user.save()
            
            return render(request, 'index/index.html', {'msj': msj, 'avatar': searchAvatarUrl(request.user)})
        else:
            return render(request, 'index/editUser.html', {'formEditUser': formEditUser, 'msj': '', 'avatar': searchAvatarUrl(request.user)})
    
    formEditUser = EditUser(
        initial = {
            'username': request.user.username,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email
        }
    )
    return render(request, 'index/editUser.html', {'formEditUser': formEditUser, 'msj': '', 'avatar': searchAvatarUrl(request.user)})

def searchAvatarUrl(user):
    return Avatar.objects.filter(user = user)[0].img.url