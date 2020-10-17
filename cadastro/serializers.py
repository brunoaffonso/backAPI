from rest_framework.serializers import ModelSerializer
from cadastro.models import Cadastro


class CadastroSerializer(ModelSerializer):
    class Meta:
        model = Cadastro
        fields = ['id', 'firstname', 'lastname', 'dob']


class CadastroMiniSerializer(ModelSerializer):
    class Meta:
        model = Cadastro
        fields = ['id', 'firstname', 'lastname']