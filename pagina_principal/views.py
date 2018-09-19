# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from .models import Pessoa
from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'index.html')

def home_com_nome(request, nome_pessoa):
	return render(request, 'index_nome.html', nome_pessoa)
