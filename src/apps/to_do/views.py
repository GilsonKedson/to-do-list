from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_user(request):
    email = request.POST['email']
    password = request.POST['password']
    
    try:
        user = User.objects.get(email=email)
        username = user.username
    except:
        messages.error(request, 'Email inválido!')
    
    user_auth = authenticate(username, password)
    
    if user_auth is not None:
        login(request, user_auth)
        messages.success(request, 'Usuário logado com sucesso!')
        return redirect('dashboard')
    else:
        messages.error(request, 'Credenciais inválidas!')
    
    return redirect('index')


def logout_user(request):
    logout(request)
    messages.success(request, 'Usuário deslogado com sucesso!')
    
    return redirect('index')