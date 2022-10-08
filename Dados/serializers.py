from rest_framework import serializers

from .models import Dados


class DadosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dados
        fields = [
            "id",
            "tipo",
            "data",
            "valor",
            "cpf",
            "cartao",
            "hora",
            "dono_da_loja",
            "nome_loja",
        ]

    def create(self, validated_data):
        print(validated_data)
        return Dados.objects.create(**validated_data)
