#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

class Funcionario(models.Model):
    '''
        @Funcionario: Modelo para uma nova pessoa
    ''' 
    nome	  = models.CharField(max_length=100)
    cpf       = models.CharField(max_length=14,blank=True,null=True,verbose_name='CPF',unique=True)
    telefone  = models.CharField(max_length=14,blank=True,null=True)
    celular   = models.CharField(max_length=14,blank=True,null=True)
    ativo     = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s %s' % (self.nome)