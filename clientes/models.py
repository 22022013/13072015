#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User,Group

TIPO_CLIENTE = (
    ('fisica','Pessoa Física'),
    ('juridica','Pessoa Jurídica'),
)

class Cliente(models.Model):
    '''
        @Cliente: Modelo para um cliente
    ''' 
    nome            = models.CharField(max_length=100)
    tipo_cliente    = models.CharField(max_length=10,choices=TIPO_CLIENTE)
    cpf             = models.CharField(max_length=14,blank=True,null=True,verbose_name='CPF',unique=True)
    cnpj            = models.CharField(max_length=18,blank=True,null=True,verbose_name='CNPJ',unique=True)
    telefone        = models.CharField(max_length=14,blank=True,null=True)
    telefone2       = models.CharField(max_length=14,blank=True,null=True)
    email           = models.EmailField(blank=True,null=True)

    ativo           = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s' % (self.nome)
    class Meta:
        db_table = u'cliente'
