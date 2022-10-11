from platform import libc_ver

from rest_framework import status
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework.views import APIView, Response

from dados.models import Dados

from .serializers import DadosSerializers


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

    def get(self, request):
        dados = Dados.objects.all()

        saldo_em_conta = 0
        soma = 0
        menos = 0

        lista_lojas_debito = []
        lista_lojas_boleto = []
        lista_lojas_financiamento = []
        lista_lojas_credito = []
        lista_lojas_re = []
        lista_lojas_vendas = []
        lista_lojas_rt = []
        lista_lojas_rd = []
        lista_lojas_aluguel = []
        lista_lojas = []
        loja = {}
        for item in dados:
            loja = dict(
                loja=item.nome_loja, tipo=item.tipo, valor=(int(item.valor) / 100.00)
            )
            lista_lojas = lista_lojas + [loja]
            if (
                item.tipo == "1"
                or item.tipo == "4"
                or item.tipo == "5"
                or item.tipo == "6"
                or item.tipo == "7"
                or item.tipo == "8"
            ):
                soma += int(item.valor) / 100.00

            else:
                menos -= int(item.valor) / 100.00

        saldo_em_conta = soma + menos
        return Response({"Transações": lista_lojas, "SALDO EM CONTA": saldo_em_conta})
