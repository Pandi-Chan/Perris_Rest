from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User
from Sistema.models import Persona, Mascota
from . import serializers

# Create your views here.

# class PersonaView(generics.ListCreateAPIView):
#     queryset = models.Persona.objects.all()
#     serializer_class = serializers.PersonaSerializer

class PersonaView(APIView):
    def get(self,request):
        personas = Persona.objects.all()
        serializer = serializers.PersonaSerializer(personas,many=True)
        return Response(serializer.data)

    def post(self,request):
        rut = request.POST.get('rut')
        clave = request.POST.get('clave')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        fechaNac = request.POST.get('fechaNacimiento')
        fono = request.POST.get('numeroFono')
        region = request.POST.get('region')
        ciudad = request.POST.get('ciudad')
        vivienda = request.POST.get('tipo')
        usuario = User.objects.create_user(username = rut, password= clave, email=email)
        persona=Persona(usuario=usuario,nombrePersona=nombre,apellidoPersona=apellido,fechaNacimiento=fechaNac,numeroFono=fono,regionPersona=region,ciudadPersona=ciudad,viviendaPersona=vivienda)
        persona.save()
        return Response()


class PerroView(APIView):
    def get(self,request):
        perros = Mascota.objects.all()
        serializer = serializers.MascotaSerializer(perros,many=True)
        return Response(serializer.data)

    def post(self,request):
        foto = request.POST.get('foto')
        nombre = request.POST.get('nombre')
        raza = request.POST.get('raza')
        descripcion = request.POST.get('descripcion')
        estado = request.POST.get('estado')
        perro=Mascota(imagen=foto,nombreMascota=nombre,razaMascota=raza,descripcion=descripcion,estadoMascota=estado)
        perro.save()
        return Response()
 