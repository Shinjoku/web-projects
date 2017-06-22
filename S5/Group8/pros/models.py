from django.db import models
from datetime import datetime


class Empresa(models.Model):
    
    nome_empresa = models.CharField(max_length=200)
    nome_social = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=20, unique=True)
    insc_estadual = models.CharField(max_length=20)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    end = models.CharField(max_length=300)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return self.nome_empresa


class Cliente(models.Model):
    
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    solicitante = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100, blank=True)
    tel = models.CharField(max_length=50)
    ramal = models.CharField(max_length=50)
    cel = models.CharField(max_length=50)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.solicitante


class Ordem(models.Model):

    # O id está implícito na criação da tabela e será usado como número da ordem serviço;
    empresa = models.CharField(max_length=200)
    cliente = models.CharField(max_length=200)
    arquivo = models.FileField(blank=True, null=True)
    data = models.DateField(default=datetime.now(), blank=True, null=True)
    num_nf_entrada = models.CharField(max_length=20, blank=True, null=True)
    descricao = models.CharField(max_length=512, blank=True, null=True)
    acessorios = models.CharField(max_length=200, blank=True, null=True)
    observacoes = models.CharField(max_length=200, blank=True, null=True)
    data_envio_orcamento = models.CharField(max_length=12, blank=True, null=True)
    data_aprovacao = models.CharField(max_length=12, blank=True, null=True)
    num_pedido = models.CharField(max_length=100, blank=True, null=True)
    valor = models.IntegerField(blank=True, null=True)
    executante = models.CharField(max_length=100, blank=True, null=True)
    data_liberacao = models.CharField(max_length=12, blank=True, null=True)
    num_nf_servico = models.CharField(max_length=20, blank=True, null=True)
    num_nf_vendas = models.CharField(max_length=20, blank=True, null=True)
    num_nf_devolucao = models.CharField(max_length=20, blank=True, null=True)
    responsavel_preenchimento = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.id