from django.conf import settings
from django.db import models
from django.utils import timezone

class CategoriaProduto(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100, primary_key=True)
    codigo = models.CharField(max_length=100)
    codigo_barras = models.CharField(max_length=150)
    categoria = models.ForeignKey('CategoriaProduto', on_delete=models.CASCADE)
    valor_venda = models.CharField(max_length=10)
    custo_medio = models.CharField(max_length=10)
    data_cadastro = models.DateField()
    unidade_medida = models.CharField(max_length=100)
    ncm = models.CharField(max_length=100)
    cest = models.CharField(max_length=100)
    peso_liquido = models.CharField(max_length=100)
    peso_bruto = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Estoque(models.Model):
    produto  = models.ForeignKey(Produto, on_delete=models.CASCADE)
    estoque_disponivel = models.CharField(max_length=10)
    estoque_minimo = models.CharField(max_length=10)
    estoque_maximo = models.CharField(max_length=10)
    data_de_cadastro = models.CharField(max_length=10)
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)

class Contato(models.Model):
    celular = models.CharField(max_length=200, null=False, blank=False)
    email = models.IntegerField(null=False, blank=False)
    telefone = models.CharField(max_length=200, null=False, blank=False)
    telefone_comercial = models.CharField(max_length=200, null=False, blank=False)

class Endereco(models.Model):
    rua = models.CharField(max_length=200, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    complemento = models.CharField(max_length=200, null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    pais = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.rua

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    endereco = models.ForeignKey('Endereco', on_delete=models.CASCADE)
    contato = models.ForeignKey('Contato', on_delete=models.CASCADE)

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=100)

class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length=25)

class FornecedorPF(PessoaFisica):
    data_inicio = models.DateField()
