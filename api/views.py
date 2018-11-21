from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

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

class PerroView(APIView):
    def get(self,request):
        perros = Mascota.objects.all()
        serializer = serializers.MascotaSerializer(perros,many=True)
        return Response(serializer.data)
