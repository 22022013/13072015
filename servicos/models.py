#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

UNIDADE = (
    ('1','UND'),
    ('2','M'),
)

class TipoServico(models.Model):
    '''
        @SubtipoServico: Modelo para tipo de servico
    ''' 
    nome  	= models.CharField(max_length=100)
    ativo   = models.BooleanField(default=True)
    
    def __unicode__(self):
        return '%s' % (self.nome)

    class Meta:
        db_table = u'tipo_servico'
        ordering = ['nome']
        
class Servico(models.Model):
    '''
        @Servico: Modelo para servico
    ''' 
    nome  	= models.CharField(max_length=100)
    tipo    = models.ForeignKey(TipoServico,blank=True,null=True,related_name="tipo_servico")
    unidade = models.CharField(max_length=1,blank=True,null=True,choices=UNIDADE)
    ativo   = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s' % (self.nome)

    class Meta:
        db_table = u'servico'
        ordering = ['nome']