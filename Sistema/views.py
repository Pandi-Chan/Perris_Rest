from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
# Correos
from django.core.mail import send_mail
# Validaciones
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
# Importacion de Modelos
from .models import Persona, Mascota
# Importacion de Formularios
from .forms import LoginForm, RecuperacionForm, RestablecerForm

# Create your views here.
#------------------------------------------ INDEX ------------------------------------------
def index(request):
    plantilla=loader.get_template("index.html")
    return HttpResponse(plantilla.render({'titulo':"Mis Perris"},request))

#------------------------------------------ WORKER ------------------------------------------
def base_layout(request,postid):
    # QUIERO QUE MAQUETA HTML CAMBIE DEPENDIENDO LA PAG QUE ESTÁ ACTUALMENTE
  template="maqueta.html"
  return render(request,template)

# ------------------------------------------ FORMULARIOS ------------------------------------------
# Registro de Personas (DESDE FUERA DEL SISTEMA, USUARIOS NUEVOS)
def registroPersona(request):
    registro=1 #Dependiendo este número, es el Formulario que Mostrará
    return render(request,"registro.html",{'registro':registro,'titulo':"Registro",})

# Registro de Personas para Admin (DESDE DENTRO DEL SISTEMA)
@login_required(login_url='login')
def registroAdmin(request):
    actual=request.user
    registro=2 # Dependiendo este Numero es el Formulario que Mostrará
    return render(request,"registro.html",{'actual':actual,'registro':registro,'titulo':"Registro",})

# Registro de Perro NUEVO (RESCATADO O DISPONIBLE)
@login_required(login_url='login')
def registroPerro(request):
    actual=request.user
    return render(request, "registroPerro.html", {'actual':actual,'titulo':"Registro Perro",})

# Registro de Mascota (ADOPCION)
# REGISTRO DE MASCOTA CON PERSONA
# ARREGLARR--------------------------------------------------
# def registroPerro(request):
#     perros=Mascota.objects.all()
#     form=RegistrarMascotaForm(request.POST, request.FILES)
#     if form.is_valid():
#         data=form.cleaned_data
#         regDB=Mascota(imagen=data.get("imagen"),nombreMascota=data.get("nombreMascota"),razaMascota=data.get("razaMascota"),descripcionMascotra=data.get("descripcionMascotra"),estadoMascota=data.get("estadoMascota"))
#         regDB.save()
#     form = RegistrarMascotaForm()
#     return render(request, "registroPerro.html", {'form': form, 'perros':perros,'titulo':"Registro Adopcion",})

# ------------------------------------------ AUTENTICACIONES y USUARIOS ------------------------------------------
# Login
def ingreso(request):
    mensaje=""
    form=LoginForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        usu=authenticate(username=data.get("username"),password=data.get("password"))
        if usu is not None:
            login(request,usu)
            return redirect('/index')
        else:
            mensaje='Datos Invalidos'
    return render(request,"login.html",{'form':form,'titulo':"Login",'mensaje':mensaje})

# Logout
def salir(request):
    logout(request)
    return redirect('/index/')

# Recuperacion Contraseña
def olvido(request):
    form=RecuperacionForm(request.POST or None)
    mensaje=""
    if form.is_valid():
        data=form.cleaned_data
        user=User.objects.get(username=data.get("username"))
        send_mail(
                'Recuperación de contraseña',
                'Haga click aquí para ingresar una nueva contraseña',
                'perrisfeos@gmail.com',
                [user.email],
                html_message = 'Pulse <a href="http://localhost:8000/restablecer?user='+user.username+'">aquí</a> para restablecer su contraseña.',
            )
        mensaje='Correo Enviado a '+user.email
    return render(request,"olvido.html",{'form':form, 'mensaje':mensaje, 'titulo':"Recuperar Contraseña",})

# Restablecer Contraseña
def restablecer(request):
    form=RestablecerForm(request.POST or None)
    mensaje=""
    try:
        username=request.GET["user"]
    except Exception as e:
        username= None
    if username is not None:
        if form.is_valid():
            data=form.cleaned_data
            if data.get("password_A") == data.get("password_B"):
                mensaje="La contraseña se ha restablecido"
                contra=make_password(data.get("password_B"))
                User.objects.filter(username=username).update(password=contra)
            else:
                mensaje="Las contraseñas no coinciden"
        return render(request,"restablecer.html",{'form':form, 'username':username, 'mensaje':mensaje, 'titulo':"Restablecer Contraseña",})
    else:
        return redirect('/login/')

# ------------------------------------------ GESTION ------------------------------------------
# Lista de Perros
@login_required(login_url='login')
def listaPerro(request):
    actual=request.user
    return render (request,"listaPerro.html",{'actual':actual,'titulo':"Lista de Perros",})

# Borrar Perro
def borrarPerro(request, postid):
    objeto=Mascota.objects.filter(codigoMascota=postid)
    objeto.delete()
    return redirect("/listaPerro/")

# Lista de Personas
@login_required(login_url='login')
def listaPersona(request):
    actual=request.user
    return render (request,"listaPersona.html",{'actual':actual,'titulo':"Lista de Personas",})
