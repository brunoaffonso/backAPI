from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from cadastro.models import Cadastro
from cadastro.serializers import CadastroSerializer, CadastroMiniSerializer


class CadastroViewSet(ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer
    #permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, )

    def list(self, request, *args, **kwargs):
        queryset = Cadastro.objects.all()
        serializer = CadastroMiniSerializer(queryset, many=True)
        return Response(serializer.data)