from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import FornecedorForm, CategoriaProdutoForm, ProdutoForm, EstoqueForm, EquipamentoForm
from .models import Fornecedor, CategoriaProduto, Produto, Estoque, Equipamento

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'home/home.html', {})

@login_required
def fornecedor_new(request):
    if request.method == "POST":
        form = FornecedorForm(request.POST)
        if form.is_valid():
            fornecedor = form.save(commit=False)
            fornecedor.save()
            return render(request, 'blog/fornecedor_edit.html', {'form': form})
    else:
       form = FornecedorForm()
       return render(request, 'blog/fornecedor_edit.html', {'form': form})

@login_required
def produto_new(request):
     if request.method == "POST":
         form = ProdutoForm(request.POST)
         if form.is_valid():
             produto = form.save(commit=False)
             produto.data_cadastro = timezone.now()
             logger.info("Data de cadastro %s",  produto.data_cadastro)
             produto.save()
             return render(request, 'blog/produto_edit.html', {'form': form})
     else:
        form = ProdutoForm()
        return render(request, 'blog/produto_edit.html', {'form': form})

@login_required
def categoria_produto_new(request):
     if request.method == "POST":
         form = CategoriaProdutoForm(request.POST)
         if form.is_valid():
             categoria = form.save(commit=False)
             categoria.save()
             return render(request, 'blog/categoria_produto_edit.html', {'form': form})
     else:
        form = CategoriaProdutoForm()
        return render(request, 'blog/categoria_produto_edit.html', {'form': form})

@login_required
def equipamento_new(request):
     if request.method == "POST":
         form = EquipamentoForm(request.POST)
         if form.is_valid():
             equipamento = form.save(commit=False)
             equipamento.save()
             return render(request, 'equipamento/equipamento_edit.html', {'form': form})
     else:
        form = Equipamento()
        return render(request, 'equipamento/equipamento_edit.html', {'form': form})

@login_required
def estoque_new(request):
    if request.method == "POST":
        form = EstoqueForm(request.POST)
        if form.is_valid():
            estoque = form.save(commit=False)
            estoque.save()
            return render(request, 'blog/estoque_edit.html', {'form': form})
    else:
       form = EstoqueForm()
       return render(request, 'blog/estoque_edit.html', {'form': form})



def home_view(request):
    return render(request, 'home.html')

def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'registration/signup.html', {'form': form})

def valida_cpf(cpf):
    if len(cpf) < 11:
        return False

    if cpf in [s * 11 for s in [str(n) for n in range(10)]]:
        return False

    calc = [i for i in range(1, 10)]
    d1= (sum([int(a)*b for a,b in zip(num[:-2], calc)]) % 11) % 10
    d2= (sum([int(a)*b for a,b in zip(reversed(num[:-2]), calc)]) % 11) % 10
    return str(d1) == num[-2] and str(d2) == num[-1]

def cpf_e_Valido(self, cpf):
    if len(cpf) == 11:
        validador = CPF()
        return validador.validate(cpf)
    else:
        return ValueError("Quantidade de digitos inválida")

@login_required
def cnpj_e_valido(self, cnpj):
    if len(cnpj) == 14:
        validate_cnpj = CNPJ()
        return validate_cnpj.validate(cnpj)
    else:
        return ValueError("Quantidade de digitos inválida")

@login_required
def produto_list(request):
    produtos = Produto.objects.all()
    categorias = CategoriaProduto.objects.all()
    return render(request, 'produto/produto_list.html', {'produtos': produtos, 'categorias': categorias})

@login_required
def fornecedor_list(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedor/fornecedor_list.html', {'fornecedores': fornecedores})
