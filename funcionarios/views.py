#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse as r
from django.contrib.auth.decorators import login_required

from core.views import group_required,verifica_membro
from .models import Funcionario,Funcao
from .forms import FuncionarioForm,FuncaoForm


def funcionarios(request):
    '''
      @funcionarios: Metodo de listagem dos funcionarios cadastrados no sistema 
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
            funcionario.notify_novo_funcionario()
            


            return HttpResponseRedirect( r('funcionarios:funcionarios'))
        else:  
            return render(request,'funcionario_cad.html',{'form': formFuncionario,'status':"Cadastrar"})
    else:
        return render(request,'funcionario_cad.html',{'form': FuncionarioForm(),'status':"Cadastrar"})

def funcao_nova_modal(request):
    '''
        @funcao_nova_modal: 
    '''
   
    if request.method == 'POST':
        form = FuncaoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)    
            obj.save()
            # Retornando para o Form que o formulario foi gravado com sucesso
            return HttpResponse(simplejson.dumps({'status':'OK'}))                                                          
        else:
            errors = form.errors
            return HttpResponse(simplejson.dumps(errors)) 
    else:
        return render(request, 'funcao_modal.html',{'form': FuncaoForm()})

def get_funcoes(request):
    if request.method == 'GET':
        funcoes = Funcao.objects.filter(ativo=True)
        funcao_dict = {}
    
        for funcao in funcoes:
            funcao_dict[funcao.id] = funcao.nome
    
        return HttpResponse(simplejson.dumps(funcao_dict))    

def funcionario_editar(request,id):
    '''
      @funcionario_editar: Metodo de edição de um funcionario cadastrado na base
    '''
    funcionario = Funcionario.objects.get(id=id)

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


def funcionario_alterar_status(request,id):
    '''
        @funcionario_alterar_status: View para alterar o status de um caderno
    '''
    funcionario = Funcionario.objects.get(id=id)

    if funcionario.ativo:
        funcionario.ativo = False
    else:       
        funcionario.ativo = True

    funcionario.save()

    return HttpResponseRedirect(r('funcionarios:funcionarios'))


def funcoes(request):
    '''
      @funcoes: Metodo de listagem dos funcionarios cadastrados no sistema 
    '''
    funcoes = Funcao.objects.filter(ativo=True).order_by('nome') 
         
    return render(request, 'funcoes.html',{'funcoes': funcoes})


def funcao_nova(request):
    '''
      @funcao_nova: Metodo de criação de uma nova Funcao 
    '''
    if request.method == 'POST':
        formFuncao = FuncaoForm(request.POST)
        if formFuncao.is_valid():
            funcao = formFuncao.save(commit=False)
            funcao.save()

            return HttpResponseRedirect( r('funcionarios:funcoes'))
        else:  
            return render(request,'funcao_cad.html',{'form': formFuncao,'status':"Cadastrar"})
    else:
        return render(request,'funcao_cad.html',{'form': FuncaoForm(),'status':"Cadastrar"})


def funcao_editar(request,id):
    '''
      @funcao_editar: Metodo de edição de uma funcao cadastrada na base
    '''
    funcao = Funcao.objects.get(id=id)

    if request.method == 'POST':

        formFuncao = FuncaoForm(request.POST,instance=funcao)
        if formFuncao.is_valid():            
            funcao = formFuncao.save(commit=False)
            funcao.save()
            
            return HttpResponseRedirect( r('funcionarios:funcoes'))
        else :
            return render(request, 'funcao_cad.html', { 'form':formFuncao ,'status':"Editar"})
    else:           
        return render(request,'funcao_cad.html',{'form': FuncaoForm(instance=funcao),'status':"Editar"})


def funcao_alterar_status(request,id):
    '''
        @funcao_alterar_status: View para alterar o status de um caderno
    '''
    funcao = Funcao.objects.get(id=id)

    if funcao.ativo:
        funcao.ativo = False
    else:       
        funcao.ativo = True

    funcao.save()

    return HttpResponseRedirect(r('funcionarios:funcoes'))