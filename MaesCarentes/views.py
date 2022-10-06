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
def oi(request):
    return render(request, "maec/oi.html")
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
def forms_mae(request):
    return render(request, "maec/forms_mae.html")
def eventos(request):
    return render(request, "maec/eventos.html")
def mae(request):
    return render(request, "maec/mae_perfil.html")
