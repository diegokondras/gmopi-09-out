from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

def approved_comments(self):
    return self.comments.filter(approved_comment=True)

from django.db import models

class Endereco(models.Model):
    CEP = models.CharField(max_length=100)
    Logradouro = models.CharField(max_length=300)
    Numero = models.CharField(max_length=100)
    Complemento = models.CharField(max_length=100)
    Bairro = models.CharField(max_length=100)
    Cidade = models.CharField(max_length=60)
    UF = (
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins"),
    )
    UF = models.CharField(max_length=60, choices=UF)

class Contato(models.Model):
    Telefone_comercial = models.CharField(max_length=50)
    Telefone_celular = models.CharField(max_length=50)
    Email = models.EmailField()
    Observacao = models.TextField()

class CategoriaProduto(models.Model):
    Nome = models.CharField(max_length=100)

class Produto(models.Model):
    Nome = models.CharField(max_length=100)
    Codigo = models.CharField(max_length=100)
    Codigo_de_barras_EAN = models.CharField(max_length=100)
    Categoria = models.ForeignKey(CategoriaProduto, on_delete=models.CASCADE)
    Valor_de_venda = models.CharField(max_length=100)
    Custo_medio = models.FloatField()
    Data_de_cadastro_do_produto = models.DateField()
    #Dados usados na Nota Fiscal (Opcional)
    #Unidade_de_medida = 
    #NCM = 
    #CEST = 
    #Peso_liquido = 
    #Peso_bruto = 

#Estoque
#Realizar Inventário
class Estoque(models.Model):
    produto  = models.ForeignKey(Produto, on_delete=models.CASCADE)
    Estoque_disponivel = models.FloatField()
    Estoque_minimo = models.FloatField()
    Estoque_maximo = models.FloatField()
    Data_de_cadastro = models.DateField()

class InscricaoEstadual(models.Model):
    INDICADOR_DE_INSCRICAO_ESTADUAL = (
        (0, "Contribuinte"),
        (1, "Não contribuinte,"),
        (2, "Contribuinte isento"),
    )
    Indicador_de_inscricao_estadual = models.IntegerField(choices=INDICADOR_DE_INSCRICAO_ESTADUAL)
    Inscricao_estadual = models.CharField(max_length=100)

class Pessoa(models.Model):
    class Meta:
        abstract = True
    nome = models.CharField(max_length=100)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)

class PessoaJuridica(Pessoa):
    CNPJ = models.CharField(max_length=100)
    Razao_social = models.CharField(max_length=100)
    Nome_fantasia = models.CharField(max_length=100)
    Data_de_fundacao = models.DateField()
#   Empresa isenta de Inscrição Estadual (Sim / Não)
    Inscricao_estadual = models.ForeignKey(InscricaoEstadual, on_delete=models.CASCADE)
    Inscricao_municipal = models.CharField(max_length=100)
    Inscricao_SUFRAMA = models.CharField(max_length=100)
    Optante_pelo_SIMPLES_Naconal =  models.BooleanField(default=False)

#CNAE Principal
#Natureza de Operação
#Reg. Especial de Tributação
#Empresa realiza importação de produtos  (Sim / Não)

class PessoaFisica(Pessoa):
    CPF = models.CharField(max_length=100)
    RG = models.CharField(max_length=100)
    Data_de_aniversario = models.DateField()

class Perfil_de_acesso(Pessoa):
    nome = models.CharField(max_length=100)

class Usuario(Pessoa):
    usuario = models.CharField(max_length=100)
    Perfil_de_acesso = models.ForeignKey(InscricaoEstadual, on_delete=models.CASCADE)
    Status_do_usuario = models.BooleanField(default=False)


#class Cliente(models.Model):
#       Nome do cliente
#       Tipo
#       Status do cliente
#       Email principal
#       Telefone comercial
#       Telefone celular
#       Código do cliente
#       Observações

class Fornecedor(Pessoa):
    STATUS = (
        (0, 'Ativo'),
        (1, 'Inativo'),
    )
    status_do_fornecedor = models.IntegerField(choices=STATUS)


class Marca(models.Model):
    logo = models.ImageField(upload_to='logo')

class Funcionalidade(models.Model):
    Nome = models.CharField(max_length=300)

#class Permissao_funcionalidades(models.Model):
#Funcionalidade
#Nome Funcionalidade 
#Permissão (Sim / Não)