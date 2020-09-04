from django import forms
from .models import Fornecedor, CategoriaProduto, Produto, Estoque, PessoaFisica

class FornecedorForm(forms.ModelForm):
	class Meta:
		model = Fornecedor
		fields = ('nome', )

class CategoriaProdutoForm(forms.ModelForm):

    class Meta:
        model = CategoriaProduto
        fields = ('nome', )

class ProdutoForm(forms.ModelForm):
	class Meta:
		model = Produto
		fields = ('nome', 'codigo', 'codigo_barras', 'categoria', 'valor_venda', 'custo_medio', 'data_cadastro', 'unidade_medida', 'ncm','cest', 'peso_liquido', 'peso_bruto', )

class EstoqueForm(forms.ModelForm):
	class Meta:
		model = Estoque
		fields = ('produto', 'estoque_disponivel', 'estoque_minimo', 'estoque_maximo', 'fornecedor')

class PessoaFisicaForm(forms.ModelForm):
	class Meta:
		model = PessoaFisica
		fields = ('cpf', )





