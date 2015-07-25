#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse as r
from django.contrib.auth.decorators import login_required

from funcionarios.models import Funcionario
from core.views import group_required,verifica_membro
from funcionarios.forms import FuncionarioForm


def funcionarios(request):
    '''
      @funcionario_lista: Metodo de listagem dos funcionarios cadastrados no sistema 
    '''
    # Buscando todos os Funcionarios da interface administrativa na base de dados      
    funcionarios = Funcionario.objects.all().order_by('nome') 
         
    return render(request, 'funcionarios.html',{'funcionarios': funcionarios})


def funcionario_novo(request):
    '''
      @funcionario_novo: Metodo de criação de um novo Funcionario 
    '''
    if request.method == 'POST':
        formFuncionario = FuncionarioForm(request.POST)
        if formFuncionario.is_valid():
            funcionario = formFuncionario.save(commit=False)
            funcionario.save()

            return HttpResponseRedirect( r('funcionarios:funcionarios'))
        else:  
            return render(request,'funcionario_cad.html',{'form': formFuncionario,'status':"Cadastrar"})
    else:
        return render(request,'funcionario_cad.html',{'form': FuncionarioForm(),'status':"Cadastrar"})


def funcionario_editar(request,id_funcionario):
    '''
      @funcionario_editar: Metodo de edição de um funcionario cadastrado na base
    '''
    funcionario = Funcionario.objects.get(id=id_funcionario)

    if request.method == 'POST':

        formFuncionario = FuncionarioForm(request.POST,instance=funcionario)
        if formFuncionario.is_valid():            
            funcionario = formFuncionario.save(commit=False)
            funcionario.save()
            
            return HttpResponseRedirect( r('funcionarios:funcionarios'))
        else :
            return render(request, 'funcionario_cad.html', { 'form':formFuncionario ,'status':"Editar"})
    else:           
        return render(request,'funcionario_cad.html',{'form': FuncionarioForm(instance=funcionario),'status':"Editar"})


def funcionario_alterar_status(request,id_funcionario):
    '''
        @funcionario_alterar_status: View para alterar o status de um caderno
    '''
    funcionario = Funcionario.objects.get(id=id_funcionario)

    if funcionario.ativo == True:
        funcionario.ativo = False
    else:       
        funcionario.ativo = True

    funcionario.save()

    return HttpResponseRedirect(r('funcionarios:funcionarios'))