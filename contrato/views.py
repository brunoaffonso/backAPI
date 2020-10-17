from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from contrato.models import Contrato
from contrato.serializers import ContratoSerializer, ContratoMiniSerializer


class ContratoViewSet(ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    #permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, )

    def list(self, request, *args, **kwargs):
        queryset = Contrato.objects.all()
        serializer = ContratoMiniSerializer(queryset, many=True)
        return Response(serializer.data)

