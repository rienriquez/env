"""Control_escolar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from core import views as core_views
from login import views as login_views


urlpatterns = [
    path('', login_views.login, name="login"),
    path('password_reset',login_views.password_reset, name='password_reset'),
    path('Bienvenida', core_views.index, name="index"),
    path('Datos_generales', core_views.Datos_generales, name="Datos_generales"),
    path('Datos_medicos/', core_views.Datos_medicos, name="Datos_medicos"),
    path('Editar_Datos_generales/', core_views.Editar_Datos_generales, name="Editar_Datos_generales"),
    path('Editar_Datos_medicos/', core_views.Editar_Datos_medicos, name="Editar_Datos_medicos"),
    path('Documentacion/', core_views.Documentacion, name="Documentacion"),
    path('Formato_inscripcion/', core_views.Formato_inscripcion, name="Formato_inscripcion"),
    path('Calificaciones/', core_views.Calificaciones, name="Calificaciones"),
    path('Boletas/', core_views.Boletas, name="Boletas"),
    path('Registro_tesis/', core_views.Registro_tesis, name="Registro_tesis"),
    path('Editar_registro_tesis',core_views.Editar_registro_tesis, name="Editar_registro_tesis"),
    path('Liberacion_tesis/', core_views.Liberacion_tesis, name="Liberacion_tesis"),
    path('Carta_liberacion/', core_views.Carta_liberacion, name="Carta_liberacion"),
    path('admin/', admin.site.urls),
    ]
    
