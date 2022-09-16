from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "maec/index.html")
def apoiador(request):
    return render(request, "maec/apoiador.html")
def editar_ap(request):
    return render(request, "maec/editar_ap.html")
def forms_pro(request):
    return render(request, "maec/forms_pro.html")
def doar(request):
    return render(request, "maec/doar.html")
def pix(request):
    return render(request, "maec/pix.html")
def boleto(request):
    return render(request, "maec/boleto.html")
def cartao(request):
    return render(request, "maec/cartao.html")
def conta(request):
    return render(request, "maec/conta.html")
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
def cadastre_se(request):
    return render(request, "maec/cadastre_se.html")
