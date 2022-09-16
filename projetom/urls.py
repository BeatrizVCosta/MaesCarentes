"""projetom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from MaesCarentes.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio, name="url_inicio"),
    path('apoiador/', apoiador, name="url_apoiador"),
    path('funcionario/', funcionario, name="url_funcionario"),
    path('cadastrar_evento/', forms_evento, name="url_cadastrar_evento"),
    path('editar/', editar, name="url_editar"),
    path('ver_maes/', tabela_m, name="url_ver_maes"),
    path('produtos_disponiveis/', tabela_p, name="url_produtos_disponiveis"),
    path('cadastrar_funcionario/', forms_fun, name="url_cadastrar_funcionario"),
    path('cadastrar_mae/', forms_mae, name="url_cadastrar_mae"),
    path('login/', login, name="url_login"),
      path('cadastre_se/', cadastre_se, name="url_cadastre_se"),
    path('editar_ap/', editar_ap, name="url_editar_ap"),
    path('doar_produto/', forms_pro, name="url_doar_produto"),
    path('doar/', doar, name="url_doar"),

]
