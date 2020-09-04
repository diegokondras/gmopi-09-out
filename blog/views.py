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
 
