#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse as r

from .models import Obra
from .forms import ObraForm

def obras(request):
    '''
      @obras: Metodo de listagem dos obras cadastrados no sistema 
    '''
    # Buscando todos os Obras da interface administrativa na base de dados      
    obras = Obra.objects.filter(ativo=True)
         
    return render(request, 'obras.html',{'obras': obras})

def obra_nova(request):
    '''
      @obra_novo: Metodo de criação de um novo Obra
    '''
    if request.method == 'POST':
        formObra = ObraForm(request.POST)
        if formObra.is_valid():
            obra = formObra.save(commit=False)
            obra.save()

            return HttpResponseRedirect( r('obras:obras'))
        else:  
            return render(request,'obra_cad.html',{'form': formObra, 'status':'Cadastrar'})
    else:
        return render(request,'obra_cad.html',{'form': ObraForm(),'status':'Cadastrar'})

def obra_editar(request,id):
    '''
      @obra_editar: Metodo de edição de um obra cadastrado na base
    '''
    obra = Obra.objects.get(id=id)

    if request.method == 'POST':

        formObra = ObraForm(request.POST,instance=obra)
        if formObra.is_valid():            
            obra = formObra.save(commit=False)
            obra.save()
            
            return HttpResponseRedirect( r('obras:obras'))
        else :
            return render(request, 'obra_cad.html', { 'form':formObra ,'obra_id':id, 'status':'Editar'})
    else:           
        return render(request,'obra_cad.html',{'form': ObraForm(instance=obra),'obra_id':id, 'status':'Editar'})

def obra_alterar_status(request,id):
    '''
        @obra_alterar_status: View para alterar o status de um obra
    '''
    obra = Obra.objects.get(id=id)

    if obra.ativo:
        obra.ativo = False
    else:       
        obra.ativo = True

    obra.save()

    return HttpResponseRedirect(r('obras:obras'))

