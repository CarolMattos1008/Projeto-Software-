<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
=======
from django.shortcuts import render
from .models import Resumo
from django.db.models import Q 
from django.views.generic.base import View
>>>>>>> 32d5fe0b6101f45bd554a29bac563782584a286a

def home(request):
    '''
    View function for home page of site.
    Renders the home.html template.
    '''
    return render(request, 'MeuSite/home.html')
<<<<<<< HEAD
    

def login_view(request):
    '''
    View function for login page.
    Handles POST to authenticate user and redirects to home on success.
    '''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'MeuSite/login.html', {'error': 'Credenciais inválidas'})

    return render(request, 'MeuSite/login.html')


def signup_view(request):
    '''
    View function for signup page.
    Handles POST to create new user and redirects to login on success.
    '''
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        # Validate inputs
        if not username or not email or not password or not password_confirm:
            return render(request, 'MeuSite/signup.html', {'error': 'Todos os campos são obrigatórios'})

        if password != password_confirm:
            return render(request, 'MeuSite/signup.html', {'error': 'As senhas não coincidem'})

        if len(password) < 6:
            return render(request, 'MeuSite/signup.html', {'error': 'A senha deve ter pelo menos 6 caracteres'})

        if User.objects.filter(username=username).exists():
            return render(request, 'MeuSite/signup.html', {'error': 'Usuário já existe'})

        if User.objects.filter(email=email).exists():
            return render(request, 'MeuSite/signup.html', {'error': 'Email já cadastrado'})

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, 'Conta criada com sucesso! Faça login para continuar.')
        return redirect('login')

    return render(request, 'MeuSite/signup.html')
=======

class ResumoListView(View):

    def get(self, request, *args, **kwargs):
        resumos = Resumo.objects.all().order_by('-data_criacao')
        contexto = {'pessoas': resumos}        
        return render(request, 'MeuSite/listaResumos.html', contexto)
    
def resultadoBusca(request):
    titulo_busca = request.GET.get('titulo')
    resumos = Resumo.objects.all()

    if titulo_busca:
        resumos = resumos.filter(Q(titulo__icontains=titulo_busca))
        
    contexto = {'pessoas': resumos}
    return render(request, 'MeuSite/listaResumos.html', contexto)
>>>>>>> 32d5fe0b6101f45bd554a29bac563782584a286a
