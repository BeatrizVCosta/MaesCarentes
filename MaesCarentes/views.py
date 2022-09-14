from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "maec/index.html")
def apoiador(request):
    return render(request, "maec/apoiador.html")
def funcionario(request):
    return render(request, "maec/funcionario.html")
def forms_evento(request):
    return render(request, "maec/forms_evento.html")
def editar(request):
    return render(request, "maec/editar_perfil.html")
def tabela_m(request):
    return render(request, "maec/tabela_maes.html")
def tabela_p(request):
    return render(request, "maec/tabela_pro.html")
def forms_fun(request):
    return render(request, "maec/forms_fun.html")
def forms_mae(request):
    return render(request, "maec/forms_mae.html")
def login(request):
    return render(request, "maec/login.html")
