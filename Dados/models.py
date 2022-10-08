from django.db import models


class transaction(models.TextChoices):
    D = "Débito"
    B = "Boleto"
    F = "Financiamento"
    C = "Crédito"
    RE = "Recebimento Empréstimo"
    V = "Vendas"
    RTED = "Recebimento TED"
    RDOC = "Recebimento DOC"
    A = "Aluguel"
    DEFAULT = "Nada"


class Dados(models.Model):
    tipo = models.CharField(max_length=2)
    data = models.CharField(max_length=8)
    valor = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.CharField(max_length=6)
    dono_da_loja = models.CharField(max_length=14)
    nome_loja = models.CharField(max_length=19)
