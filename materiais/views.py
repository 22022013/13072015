#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse as r

from materiais.models import Material
from materiais.forms import MaterialForm

import hashlib, time, simplejson



def materiais(request):
    '''
      @materiais: Metodo de listagem dos materiais cadastrados no sistema 
    '''
    # Buscando todos os Materials da interface administrativa na base de dados      
    materiais = Material.objects.filter(ativo=True).order_by('nome') 
         
    return render(request, 'materiais.html',{'materiais': materiais})

def material_novo(request):
    '''
      @material_novo: Metodo de criação de um novo Material
    '''
    if request.method == 'POST':
        formMaterial = MaterialForm(request.POST)
        if formMaterial.is_valid():
            material = formMaterial.save(commit=False)
            material.save()

            return HttpResponseRedirect( r('materiais:materiais'))
        else:  
            return render(request,'material_cad.html',{'form': formMaterial, 'status':'Cadastrar'})
    else:
        return render(request,'material_cad.html',{'form': MaterialForm(),'status':'Cadastrar'})

def material_novo_modal(request):
    '''
        @material_novo_modal: 
    '''
   
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)    
            obj.save()
            # Retornando para o Form que o formulario foi gravado com sucesso
            return HttpResponse(simplejson.dumps({'status':'OK'}))                                                          
        else:
            errors = form.errors
            return HttpResponse(simplejson.dumps(errors)) 
    else:
        return render(request, 'material_modal.html',{'form': MaterialForm()})

def material_editar(request,material_id):
    '''
      @material_editar: Metodo de edição de um material cadastrado na base
    '''
    material = Material.objects.get(id=material_id)

    if request.method == 'POST':

        formMaterial = MaterialForm(request.POST,instance=material)
        if formMaterial.is_valid():            
            material = formMaterial.save(commit=False)
            material.save()
            
            return HttpResponseRedirect( r('materiais:materiais'))
        else :
            return render(request, 'material_cad.html', { 'form':formMaterial ,'material_id':material_id, 'status':'Editar'})
    else:           
        return render(request,'material_cad.html',{'form': MaterialForm(instance=material),'material_id':material_id, 'status':'Editar'})

def material_alterar_status(request,material_id):
    '''
        @material_alterar_status: View para alterar o status de um material
    '''
    material = Material.objects.get(id=material_id)

    if material.ativo == True:
        material.ativo = False
    else:       
        material.ativo = True

    material.save()

    return HttpResponseRedirect(r('materiais:materiais'))

