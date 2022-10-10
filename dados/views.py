from rest_framework import status
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework.views import APIView, Response

from .serializers import DadosSerializers

# Create your views here.


class FileUploadView(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request, filename, format=None):
        file = request.FILES["file"].read().decode().split("\n")
        file.pop()

        data_cnab = []
        for item in file:

            serializer = DadosSerializers(
                data={
                    "tipo": item[0],
                    "data": item[1:9],
                    "valor": item[9:19],
                    "cpf": item[19:30],
                    "cartao": item[30:42],
                    "hora": item[42:48],
                    "dono_da_loja": item[48:62],
                    "nome_loja": item[62:81],
                }
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data_cnab = [serializer.data] + data_cnab

        return Response(data=data_cnab, status=status.HTTP_201_CREATED)
