from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import CustomUser

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('base')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base')
        elif username == '' or password == '':
            messages.error(request, 'Debes completar todos los campos para iniciar sesión.')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'account/login.html')

def register_view(request):
    if request.method == 'POST':
        newUsername = request.POST.get('newUsername', '').strip()
        email = request.POST.get('email', '').strip()
        newPassword = request.POST.get('newPassword', '').strip()
        rePassword = request.POST.get('rePassword', '').strip()

        if not newUsername or not email or not newPassword or not rePassword:
            messages.error(request, 'Debes completar todos los campos para registrarte.')
        elif '@' not in email:
            messages.error(request, 'Debes ingresar un correo electrónico válido.')
        elif len(newPassword) < 4:
            messages.error(request, 'La contraseña debe tener más de 4 caracteres.')
        elif newPassword != rePassword:
            messages.error(request, 'Las contraseñas no coinciden.')
        elif CustomUser.objects.filter(username=newUsername).exists():
            messages.error(request, 'El nombre de usuario ya existe.')
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'El correo electrónico ya está registrado.')
        else:
            try:
                user = CustomUser.objects.create_user(
                    username=newUsername,
                    email=email,
                    password=newPassword,
                    tipo='cliente'  # forzamos el tipo cliente
                )
                messages.success(request, 'Usuario cliente creado correctamente.')
                return redirect('login')
            except IntegrityError:
                messages.error(request, 'Ocurrió un error al crear el usuario.')
    return render(request, 'account/register.html')


def account_view(request):
    if request.user.is_authenticated:
        return render(request, 'account/account.html')
    else:
        messages.error(request, 'Debes iniciar sesión para acceder a tu perfil.')
        return redirect('login')

""" NO ES UNA VISTA FISICA """
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Has cerrado sesión correctamente, esperamos verte pronto!')
        return redirect('login')
    else:
        return redirect('login')
