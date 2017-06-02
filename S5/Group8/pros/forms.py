import datetime
from localflavor.br.forms import BRCNPJField, BRPhoneNumberField, STATE_CHOICES
from django import forms
from .models import Empresa, Cliente, Ordem


class CadastrarEmpresa(forms.ModelForm):
    nome_empresa = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'nome_empresa'}))
    nome_social = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'nome_social'}))
    cnpj = BRCNPJField(max_length=18, min_length=14,
                       widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'cnpj'}))
    insc_estadual = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'insc_estadual'}))
    cidade = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'cidade'}))
    estado = forms.ChoiceField(choices=STATE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    end = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'end'}))
    cep = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'cep'}))

    class Meta:
        model = Empresa
        fields = ('nome_empresa', 'nome_social', 'cnpj', 'insc_estadual', 'cidade', 'estado', 'end', 'cep')


class CadastrarCliente(forms.ModelForm):
    solicitante = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'solicitante'}))
    responsavel = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'responsavel'}))
    cargo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'cargo'}))
    tel = BRPhoneNumberField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'tel'}))
    ramal = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'ramal'}))
    cel = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'cel'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'email', 'type': 'email'}))

    class Meta:
        model = Cliente
        fields = ('solicitante', 'responsavel', 'cargo', 'tel', 'ramal', 'cel', 'email')


class CadastrarOrdem(forms.ModelForm):
    empresa = forms.ModelChoiceField(queryset=Empresa.objects.all(), empty_label="Selecione uma Empresa",
                                     widget=forms.Select(attrs={'class': 'form-control', 'id': 'select1'}))
    data_envio = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'data_envio'}))
    data_aprovado = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'data_aprovado'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'descricao'}))
    acessorios = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'acessorios'}))
    observacoes = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'observacoes'}))
    num_pedido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'num_pedido'}))
    valor = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'valor'}))
    executante = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'executante'}))
    data_liberacao = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'data_liberacao'}))
    num_nf_entrada = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'num_nf_entrada'}))
    num_nf_servico = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'num_nf_servico'}))
    num_nf_vendas = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'num_nf_vendas'}))
    num_nf_devolucao = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'num_nf_devolucao'}))
    responsavel_preenchimento = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'responsavel_preenchimento'}))

    class Meta:
        model = Ordem
        fields = ('empresa', 'num_nf_entrada', 'descricao', 'acessorios', 'observacoes', 'data_envio', 'data_aprovado',
                  'num_pedido', 'valor', 'executante', 'data_liberacao', 'num_nf_servico', 'num_nf_vendas',
                  'num_nf_devolucao', 'responsavel_preenchimento')
