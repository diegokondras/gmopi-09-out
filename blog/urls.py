from django.urls import path
from . import views
from django.contrib import admin

from django.conf.urls import url

urlpatterns = [
	path('', views.home, name='home'),
	path('fornecedor/new/', views.fornecedor_new, name='fornecedor_new'),
    path('categoriaproduto/new/', views.categoria_produto_new, name='categoria_produto_new'),
    path('produto/new/', views.produto_new, name='produto_new'),
    path('estoque/new/', views.estoque_new, name='estoque_new'),
    path('', views.home_view, name="home"),
    path('signup/', views.signup_view, name="signup"),
]
