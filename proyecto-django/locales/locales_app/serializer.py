from rest_framework import serializers


from .models import Barrio, Persona, LocalesComida, LocalesRepuestos

class BarrioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Barrio
        fields = "__all__"


class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = "__all__"


class LocalesComidaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LocalesComida
        fields = "__all__"


class LocalesRepuestosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LocalesRepuestos
        fields = "__all__"

