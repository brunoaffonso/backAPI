from rest_framework.serializers import ModelSerializer
from contrato.models import Contrato


class ContratoSerializer(ModelSerializer):
    class Meta:
        model = Contrato
        fields = ['id', 'number', 'year', 'descricao', 'name', 'fiscal']


class ContratoMiniSerializer(ModelSerializer):
    class Meta:
        model = Contrato
        fields = ['id', 'name']