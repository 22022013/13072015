#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

class Funcao(models.Model):
    '''
        @Funcao: Modelo para uma nova funcao
    ''' 
    nome      = models.CharField(max_length=100,unique=True)
    ativo     = models.BooleanField(default=True)
   
    def __unicode__(self):
        return '%s' % (self.nome)

class Funcionario(models.Model):
    '''
        @Funcionario: Modelo para uma nova pessoa
    ''' 
    nome      = models.CharField(max_length=100)
    cpf       = models.CharField(max_length=14,blank=True,null=True,verbose_name='CPF',unique=True)
    telefone  = models.CharField(max_length=14,blank=True,null=True)
    celular   = models.CharField(max_length=14,blank=True,null=True)
    funcao    = models.ForeignKey(Funcao,blank=True,null=True,related_name="funcao")
    ativo     = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s' % (self.nome)
