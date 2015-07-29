#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse as r
from django.contrib.auth.decorators import login_required

from vegetativo.models import OrdemServico
from core.views import group_required,verifica_membro
from vegetativo.forms import OrdemServicoForm


def ordens_servico(request):
    '''
      @ordens_servico: Metodo de listagem das os cadastradas no sistema 
    '''
    
    ordens_servico = OrdemServico.objects.all()
         
    return render(request, 'ordens_servico.html',{'ordens_servico': ordens_servico})


def os_nova(request):
    '''
      @os_nova: Metodo de criação de uma ordem de servico
    '''
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            os = form.save(commit=False)
            os.save()

            return HttpResponseRedirect( r('vegetativo:ordens_servico'))
        else:  
            return render(request,'os_cad.html',{'form': form,'status':"Nova"})
    else:
        return render(request,'os_cad.html',{'form': OrdemServicoForm(),'status':"Nova"})


def os_editar(request,os_id):
    '''
      @os_editar: Metodo de edição de uma os cadastrada na base
    '''
    os = OrdemServico.objects.get(id=os_id)

    if request.method == 'POST':

        form = OrdemServicoForm(request.POST,instance=os)
        if form.is_valid():            
            os = form.save(commit=False)
            os.save()
            
            return HttpResponseRedirect( r('vegetativo:ordens_servico'))
        else :
            return render(request, 'os_cad.html', { 'form':form ,'status':"Editar"})
    else:           
        return render(request,'os_cad.html',{'form': OrdemServicoForm(instance=os),'status':"Editar"})
