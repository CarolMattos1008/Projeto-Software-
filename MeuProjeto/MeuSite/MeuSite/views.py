from django.shortcuts import render
from .models import Resumo
from django.db.models import Q 
from django.views.generic.base import View

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
    
def resultadoBusca(request):
    titulo_busca = request.GET.get('titulo')
    resumos = Resumo.objects.all()

    if titulo_busca:
        resumos = resumos.filter(Q(titulo__icontains=titulo_busca))
        
    contexto = {'pessoas': resumos}
    return render(request, 'MeuSite/listaResumos.html', contexto)