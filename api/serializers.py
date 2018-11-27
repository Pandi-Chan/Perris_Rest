from rest_framework import serializers
from Sistema.models import Persona, Mascota

class PersonaSerializer(serializers.ModelSerializer):
	# SERIALIZER DE PERSONA ( TOMA TODOS LOS CAMPOS )
    class Meta:
        fields = ('__all__')
        model = Persona

class MascotaSerializer(serializers.ModelSerializer):
	# SERIALIZER DE PERRO ( TOMA TODOS LOS CAMPOS )
    class Meta:
        fields = ('__all__')
        model = Mascota
