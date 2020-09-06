from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import FornecedorForm, CategoriaProdutoForm, ProdutoForm, EstoqueForm
from .models import Fornecedor, CategoriaProduto, Produto, Estoque

def home(request):
    return render(request, 'home/home.html', {})

@login_required
def fornecedor_new(request):
    form = FornecedorForm()
    return render(request, 'blog/fornecedor_edit.html', {'form': form})

@login_required
def produto_new(request):
    form = ProdutoForm()
    return render(request, 'blog/produto_edit.html', {'form': form})

@login_required
def categoria_produto_new(request):
    form = CategoriaProdutoForm()
    return render(request, 'blog/categoria_produto_edit.html', {'form': form})

@login_required
def estoque_new(request):
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

def cnpj_e_valido(self, cnpj):
    if len(cnpj) == 14:
        validate_cnpj = CNPJ()
        return validate_cnpj.validate(cnpj)
    else:
        return ValueError("Quantidade de digitos inválida")

 
