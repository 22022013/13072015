#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse as r

from servicos.models import TipoServico,Servico
from servicos.forms import TipoServicoForm,ServicoForm

import hashlib, time, simplejson



def servicos(request):
    '''
      @servicos: Metodo de listagem dos servicos cadastrados no sistema 
    '''
    # Buscando todos os Servicos da interface administrativa na base de dados      
    servicos = Servico.objects.filter(ativo=True).order_by('nome') 
         
    return render(request, 'servicos.html',{'servicos': servicos})

def servico_novo(request):
    '''
      @servico_novo: Metodo de criação de um novo Servico
    '''
    if request.method == 'POST':
        formServico = ServicoForm(request.POST)
        if formServico.is_valid():
            servico = formServico.save(commit=False)
            servico.save()

            return HttpResponseRedirect( r('servicos:servicos'))
        else:  
            return render(request,'servico_cad.html',{'form': formServico, 'status':'Cadastrar'})
    else:
        return render(request,'servico_cad.html',{'form': ServicoForm(),'status':'Cadastrar'})

def servico_novo_modal(request):
    '''
        @servico_novo_modal: 
    '''
   
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)    
            obj.save()
            # Retornando para o Form que o formulario foi gravado com sucesso
            return HttpResponse(simplejson.dumps({'status':'OK'}))                                                          
        else:
            errors = form.errors
            return HttpResponse(simplejson.dumps(errors)) 
    else:
        return render(request, 'servico_modal.html',{'form': ServicoForm()})

def servico_editar(request,servico_id):
    '''
      @servico_editar: Metodo de edição de um servico cadastrado na base
    '''
    servico = Servico.objects.get(id=servico_id)

    if request.method == 'POST':

        formTipoServico = ServicoForm(request.POST,instance=servico)
        if formTipoServico.is_valid():            
            servico = formTipoServico.save(commit=False)
            servico.save()
            
            return HttpResponseRedirect( r('servicos:servicos'))
        else :
            return render(request, 'servico_cad.html', { 'form':formServico ,'servico_id':servico_id, 'status':'Editar'})
    else:           
        return render(request,'servico_cad.html',{'form': ServicoForm(instance=servico),'servico_id':servico_id, 'status':'Editar'})

def servico_alterar_status(request,servico_id):
    '''
        @servico_alterar_status: View para alterar o status de um servico
    '''
    servico = Servico.objects.get(id=servico_id)

    if servico.ativo == True:
        servico.ativo = False
    else:       
        servico.ativo = True

    servico.save()

    return HttpResponseRedirect(r('servicos:servicos'))

def tipos_servico(request):
    '''
      @servicos: Metodo de listagem dos servicos cadastrados no sistema 
    '''
    # Buscando todos os Servicos da interface administrativa na base de dados      
    tipos_servico = TipoServico.objects.filter(ativo=True).order_by('nome') 
         
    return render(request, 'tipos_servico.html',{'tipos_servico': tipos_servico})

def tipo_servico_novo(request):
    '''
      @servico_novo: Metodo de criação de um novo Servico
    '''
    if request.method == 'POST':
        formTipoServico = TipoServicoForm(request.POST)
        if formTipoServico.is_valid():
            tipo_servico = formTipoServico.save(commit=False)
            tipo_servico.save()

            return HttpResponseRedirect( r('servicos:tipos_servico'))
        else:  
            return render(request,'tipo_servico_cad.html',{'form': formTipoServico, 'status':'Cadastrar'})
    else:
        return render(request,'tipo_servico_cad.html',{'form': TipoServicoForm(),'status':'Cadastrar'})

def tipo_servico_novo_modal(request):
    '''
        @servico_novo_modal: 
    '''
   
    if request.method == 'POST':
        form = TipoServicoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)    
            obj.save()
            # Retornando para o Form que o formulario foi gravado com sucesso
            return HttpResponse(simplejson.dumps({'status':'OK'}))                                                          
        else:
            errors = form.errors
            return HttpResponse(simplejson.dumps(errors)) 
    else:
        return render(request, 'tipo_servico_modal.html',{'form': TipoServicoForm()})

def get_tipos_servico(request):
    if request.method == 'GET':
        tipos_servico = TipoServico.objects.filter(ativo=True)
        tipo_servico_dict = {}
    
        for tipo_servico in tipos_servico:
            tipo_servico_dict[tipo_servico.id] = tipo_servico.nome
    
        return HttpResponse(simplejson.dumps(tipo_servico_dict))    

def tipo_servico_editar(request,tipo_servico_id):
    '''
      @servico_editar: Metodo de edição de um servico cadastrado na base
    '''
    tipo_servico = TipoServico.objects.get(id=tipo_servico_id)

    if request.method == 'POST':

        formTipoServico = TipoServicoForm(request.POST,instance=tipo_servico)
        if formTipoServico.is_valid():            
            tipo_servico = formTipoServico.save(commit=False)
            tipo_servico.save()
            
            return HttpResponseRedirect( r('servicos:tipos_servico'))
        else :
            return render(request, 'tipo_servico_cad.html', { 'form':formTipoServico ,'tipo_servico_id':tipo_servico_id, 'status':'Editar'})
    else:           
        return render(request,'tipo_servico_cad.html',{'form': TipoServicoForm(instance=tipo_servico),'tipo_servico_id':tipo_servico_id, 'status':'Editar'})

def tipo_servico_alterar_status(request,tipo_servico_id):
    '''
        @subtiposervico_alterar_status: View para alterar o status de um servico
    '''
    tipo_servico = TipoServico.objects.get(id=tipo_servico_id)

    if tipo_servico.ativo == True:
        tipo_servico.ativo = False
    else:       
        tipo_servico.ativo = True

    tipo_servico.save()

    return HttpResponseRedirect(r('servicos:tipos_servico'))