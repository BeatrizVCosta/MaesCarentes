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

from MaesCarentes.views import inicio, apoiador, funcionario, forms_evento, editar, tabela_m, tabela_p, forms_fun, forms_mae, login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio),
    path('apoiador/', apoiador),
    path('funcionario/', funcionario),
    path('cadastrar_evento/', forms_evento),
    path('funcionario/editar/', editar),
    path('ver_maes/', tabela_m),
    path('produtos_disponiveis/', tabela_p),
    path('cadastrar_funcionario/', forms_fun),
    path('cadastrar_mae/', forms_mae),
    path('login/', login),
    

]
