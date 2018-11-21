from rest_framework import serializers
from Sistema.models import Persona, Mascota

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'usuario',
            'nombrePersona',
            'apellidoPersona',
            'fechaNacimiento',
            'numeroFono',
            'regionPersona',
            'ciudadPersona',
            'viviendaPersona',
            'tipoPersona',
        )
        model = Persona

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'codigoMascota',
            'imagen',
            'nombreMascota',
            'razaMascota',
            'descripcion',
            'estadoMascota',
        )
        model = Mascota
