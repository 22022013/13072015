#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse as r
from django.contrib.auth.decorators import login_required

from core.views import group_required,verifica_membro
from .models import Cliente
from .forms import ClienteForm

@login_required
#@group_required('Administrador','Auxiliar')
def clientes(request):
    '''
      @cliente_lista: Metodo de listagem dos clientes cadastrados no sistema 
    '''
  
    clientes = Cliente.objects.filter(ativo=True).order_by('nome') 
         
    return render(request, 'clientes.html',{'clientes': clientes})

@login_required
#@group_required('Administrador','Auxiliar')
def cliente_novo(request):
    '''
      @cliente_novo: Metodo de criação de um novo Cliente 
    '''
    if request.method == 'POST':
        formCliente = ClienteForm(request.POST)
        if formCliente.is_valid():
            cliente = formCliente.save(commit=False)
            cliente.save()

            return HttpResponseRedirect( r('clientes:clientes'))
        else:  
            return render(request,'cliente_cad.html',{'form': formCliente})
    else:
        return render(request,'cliente_cad.html',{'form': ClienteForm()})


@login_required
#@group_required('Administrador','Auxiliar')
def cliente_novo_modal(request):
    '''
        @cliente_novo_modal: 
    '''
   
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)    
            obj.save()
            # Retornando para o Form que o formulario foi gravado com sucesso
            return HttpResponse(simplejson.dumps({'status':'OK'}))                                                          
        else:
            errors = form.errors
            return HttpResponse(simplejson.dumps(errors)) 
    else:
        return render(request, 'cliente_modal.html',{'form': ClienteForm()})



@login_required
#@group_required('Administrador','Auxiliar')
def cliente_editar(request,id):
    '''
      @cliente_editar: Metodo de edição de um cliente cadastrado na base
    '''
    cliente = Cliente.objects.get(id=id)

    if request.method == 'POST':

        formCliente = ClienteForm(request.POST,instance=cliente)
        if formCliente.is_valid():            
            cliente = formCliente.save(commit=False)
            cliente.save()
            
            return HttpResponseRedirect( r('clientes:clientes'))
        else :
            return render(request, 'cliente_cad.html', { 'form':formCliente ,'id_cliente':id})
    else:           
        return render(request,'cliente_cad.html',{'form': ClienteForm(instance=cliente),'id_cliente':id})


@login_required
#@group_required('Administrador','Auxiliar')
def cliente_alterar_status(request,id):
    '''
        @cliente_alterar_status: View para alterar o status de um caderno
    '''
    cliente = Cliente.objects.get(id=id)

    if cliente.ativo:
        cliente.ativo = False
    else:       
        cliente.ativo = True

    cliente.save()

    return HttpResponseRedirect(r('clientes:clientes'))

