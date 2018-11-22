from rest_framework import serializers
from Sistema.models import Persona, Mascota

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Persona

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Mascota
