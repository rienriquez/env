from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "core/index.html")

def Datos_generales(request):
    return render(request, "core/Datos_generales.html")

def Datos_medicos(request):
    return render(request, "core/Datos_medicos.html")

def Editar_Datos_generales(request):
    return render(request, "core/Editar_Datos_Generales.html")

def Editar_Datos_medicos(request):
    return render(request, "core/Editar_Datos_Medicos.html")

def Documentacion(request):
    return render(request, "core/Documentacion.html")

def Formato_inscripcion(request):
    return render(request, "core/Formato_inscripcion.html")

def Calificaciones(request):
    return render(request, "core/Calificaciones.html")

def Boletas(request):
    return render(request, "core/Boletas.html")

def Registro_tesis(request):
    return render(request, "core/Registro_tesis.html")

def Editar_registro_tesis(request):
    return render(request, "core/Editar_registro_de_tesis.html")
                                
def Liberacion_tesis(request):
    return render(request, "core/Liberacion_tesis.html")

def Carta_liberacion(request):
    return render(request, "core/Carta_liberacion.html")

def index(request):
    return render(request, "core/index.html")