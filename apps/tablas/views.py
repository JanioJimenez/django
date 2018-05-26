from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "mensaje":"holaaa",
    }
    return render(request, 'base.html', context)

def usuario(request):
    context = {"mensaje":"hola"}
    return render(request,'usuario.html', context)

def registro(request):
    context = {"mensaje":"hola"}
    return render(request,'registro.html',context)

def gmail(request):
    return render(request, 'gmail.html')

def home(request):
    return render(request, 'home.html')