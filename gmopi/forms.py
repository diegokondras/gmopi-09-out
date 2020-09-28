from django import forms
from .models import Fornecedor, CategoriaProduto, Produto, Estoque, PessoaFisica, Equipamento
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Column, Reset
from crispy_forms.bootstrap import (
    Accordion,
    AccordionGroup,
    Alert,
    AppendedText,
    FieldWithButtons,
    InlineCheckboxes,
    InlineRadios,
    PrependedAppendedText,
    PrependedText,
    StrictButton,
    Tab,
    TabHolder,
)

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ('nome', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'nome',
            ButtonHolder(
                Submit('submit', 'Salvar', css_class=''),
                Reset('reset', 'Limpar', css_class='btn-danger')
            )

        )

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ('nome', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'nome',
            ButtonHolder(
                Submit('submit', 'Salvar', css_class=''),
                Reset('reset', 'Limpar', css_class='btn-danger')
            )

        )

class CategoriaProdutoForm(forms.ModelForm):
    class Meta:
        model = CategoriaProduto
        fields = ('nome',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'nome',
            ButtonHolder(
                Submit('submit', 'Salvar', css_class=''),
                Reset('reset', 'Limpar', css_class='btn-danger')
            )
        )

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nome', 'codigo', 'codigo_barras', 'categoria', 'valor_venda', 'custo_medio', 'unidade_medida', 'ncm','cest', 'peso_liquido', 'peso_bruto', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'espessura', 'comprimento ', 'largura',
            Row (
                Column('nome', css_class='col-md-8 col-sm-12'),
                Column('categoria', css_class='col-md-4 col-sm-12')
            ),
            Row (
                Column('codigo', css_class='col-md-4 col-sm-12'),
                Column('codigo_barras', css_class='col-md-8 col-sm-12')
            ),
            Row (
                Column('ncm', css_class='col-md-6 col-sm-12'),
                Column('cest', css_class='col-md-6 col-sm-12')
            ),
            Row (
                AppendedText('valor_venda', 'R$', active=True, css_class='col-md-8 col-sm-12'),
                AppendedText('custo_medio', 'R$', active=True, css_class='col-md-8 col-sm-12')
            ),
            Row (
                Column('unidade_medida', css_class='col-md-4 col-sm-12'),
                Column('peso_liquido', css_class='col-md-4 col-sm-12'),
                Column('peso_bruto', css_class='col-md-4 col-sm-12')
            ),
            ButtonHolder(
                Submit('submit', 'Salvar', css_class=''),
                Reset('reset', 'Limpar', css_class='btn-danger')
            )
        )


class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ('produto', 'estoque_disponivel', 'estoque_minimo', 'estoque_maximo', 'fornecedor', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row (
                Column('produto', css_class='col-md-8 col-sm-12'),
                Column('fornecedor', css_class='col-md-4 col-sm-12')
            ),
            Row (
                Column('estoque_disponivel', css_class='col-md-4 col-sm-12'),
                Column('estoque_minimo', css_class='col-md-4 col-sm-12'),
                Column('estoque_maximo', css_class='col-md-4 col-sm-12')
            ),
            ButtonHolder(
                Submit('submit', 'Salvar', css_class=''),
                Reset('reset', 'Limpar', css_class='btn-danger')
            )
        )
