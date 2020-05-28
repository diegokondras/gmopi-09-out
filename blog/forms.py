from django import forms
from .models import Post, Comment, CategoriaProduto, Produto, Contato, Endereco, Estoque

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class CategoriaProdutoForm(forms.ModelForm):

    class Meta:
        model = CategoriaProduto
        fields = ('Nome',)



class ProdutoForm(forms.ModelForm):
	class Meta:
		model = Produto
		fields = ('Nome', 'Codigo', 'Codigo_de_barras_EAN', 'Categoria', 'Valor_de_venda', 'Custo_medio',)


class ContatoForm(forms.ModelForm):
	class Meta:
		model = Contato
		fields = ('Telefone_comercial', 'Telefone_celular', 'Email', 'Observacao')


class EstoqueForm(forms.ModelForm):
	class Meta:
		model = Estoque
		fields = ('produto', 'Estoque_disponivel', 'Estoque_minimo', 'Estoque_maximo',)