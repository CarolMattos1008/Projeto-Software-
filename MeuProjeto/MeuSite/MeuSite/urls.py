from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from MeuSite import views 
from MeuSite.views import ResumoListView, buscarResumo, resultadoBusca, view_login, view_cadastro

urlpatterns = [
    # Rotas Principais (Comuns)
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('app/resumos/', ResumoListView.as_view(), name='lista-resumos'),
    path('app/buscar/', buscarResumo, name='buscar-resumo'),
    path('app/resultado-busca/', resultadoBusca, name='resultado-busca'),
    path('login/', view_login, name='login'),
    path('cadastro/', view_cadastro, name='cadastro'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)