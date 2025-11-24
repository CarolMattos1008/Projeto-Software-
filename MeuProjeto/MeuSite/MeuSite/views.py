# --- IMPORTS COMBINADOS DE AMBAS AS VERSÕES ---
from django.shortcuts import render, redirect
from .models import Resumo
from django.db.models import Q 
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from django.contrib import messages
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required

# --- FUNÇÃO HOME (COMUM) ---
def home(request):
    # Busca todos os posts, do mais recente para o mais antigo
    posts = Post.objects.all().order_by('-data_criacao')
    return render(request, 'MeuSite/home.html', {'posts': posts})
    
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

    return render(request, 'MeuSite/cadastro.html', {'form': form})

@login_required(login_url='login') # Garante que só quem está logado pode postar
def criar_post(request):
    if request.method == 'POST':
        # request.FILES é necessário para upload de imagens
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # Cria o objeto mas não salva ainda
            post.autor = request.user      # Preenche o autor com o usuário logado
            post.save()                    # Agora salva no banco
            messages.success(request, "Resumo postado com sucesso!")
            return redirect('home')
    else:
        form = PostForm()
    
    return render(request, 'MeuSite/criar_post.html', {'form': form})