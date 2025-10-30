from django.db import models
from django.contrib.auth.models import User  # para associar conteúdos a usuários

class UsuarioPerfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, help_text='Fale um pouco sobre você')
    area_estudo = models.CharField(max_length=100, help_text='Sua área principal de estudo')
    foto = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username


class Resumo(models.Model):
    titulo = models.CharField(max_length=200, help_text='Título do resumo')
    conteudo = models.TextField(help_text='Escreva o conteúdo do seu resumo aqui')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumos')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    materia = models.CharField(max_length=100, help_text='Ex: Matemática, História, Biologia')

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    resumo = models.ForeignKey(Resumo, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField(help_text='Escreva seu comentário')
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor.username} em {self.resumo.titulo}"


class Material(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    arquivo = models.FileField(upload_to='materiais/')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
