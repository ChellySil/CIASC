from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'home.html')

def create(request):
    return render(request, 'create.html')

def store(request):
    data = {}
    if (request.POST['password'] >= str(8)):

        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.last_name = request.POST['last-name']
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso'
        data['class'] = 'alert-success'

    return render(request, 'create.html', data)

def painel(request):
    return render(request, 'painel.html')

def doLogin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password = request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou senha inválida'
        data['class'] = 'alert-success'
        return render(request, 'painel.html', data)

def dashboard(request):
    return render(request, 'dashboard/home.html')