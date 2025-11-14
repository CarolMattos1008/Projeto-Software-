from django.shortcuts import render, redirect
from .models import Resumo
from django.db.models import Q 
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def home(request):
    '''
    View function for home page of site.
    Renders the home.html template.
    '''
    return render(request, 'MeuSite/home.html')

class ResumoListView(View):

    def get(self, request, *args, **kwargs):
        resumos = Resumo.objects.all().order_by('-data_criacao')
        contexto = {'pessoas': resumos}        
        return render(request, 'MeuSite/listaResumos.html', contexto)
    
def buscarResumo(request):
    """
    Renderiza o template que contém o formulário de busca (buscaResumo.html)
    """
    return render(request, 'MeuSite/buscaResumo.html')
    
def resultadoBusca(request):
    titulo_busca = request.GET.get('titulo')
    resumos = Resumo.objects.all()

    if titulo_busca:
        resumos = resumos.filter(Q(titulo__icontains=titulo_busca))
        
    contexto = {'pessoas': resumos}
    return render(request, 'MeuSite/listaResumos.html', contexto)

def view_login(request):
    # Se o usuário já está logado, redireciona para a home
    if request.user.is_authenticated:
        return redirect('home')

    # Se o formulário foi enviado (método POST)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            # Se o usuário existir e a senha estiver correta
            if user is not None:
                login(request, user)
                messages.success(request, f"Bem-vindo(a) de volta, {username}!")
                return redirect('home') # Redireciona para a Home
            else:
                messages.error(request, "Usuário ou senha inválidos.")
        else:
            messages.error(request, "Usuário ou senha inválidos.")

    # Se o usuário está apenas acessando a página (método GET)
    form = AuthenticationForm()
    # Renderiza o template de login (que sua equipe 'fez')
    return render(request, 'MeuSite/login.html', {'form': form})

def view_cadastro(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # Salva o novo usuário no banco de dados
            messages.success(request, "Cadastro realizado com sucesso! Faça o login.")
            return redirect('login') # Redireciona para o Login
        else:
            messages.error(request, "Não foi possível realizar o cadastro. Verifique os erros.")

    form = UserCreationForm()
    # Renderiza o template de cadastro (que sua equipe 'fez')
    return render(request, 'MeuSite/cadastro.html', {'form': form})