from django.db import models
from django import forms
from .enum import Perfil, Estado

class Usuarios(models.Model):
    
    def usuarios_directory_path(instance,filename):
        return 'usuarios/{0}'.format(filename)
    
    id_usuario = models.BigAutoField(primary_key=True)
    nombre = models.CharField('nombre', max_length = 50)
    username = models.CharField('username', max_length = 30, unique=True)
    password = models.CharField(max_length=256)
    #passw = models.PasswordField();
    perfil = models.CharField(max_length =15, choices=Perfil.choices())
    foto = models.ImageField(upload_to=usuarios_directory_path, default="usuarios/default.png",null=True, blank=True)
    
    estado = models.CharField(max_length =15, choices=Estado.choices(), default="AC")
    ultimo_ingreso = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username