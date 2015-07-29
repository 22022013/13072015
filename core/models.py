#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

class UF(models.Model): 
    '''
        @UF: Modelo de dados com todas as UF.
    '''       
    cod   = models.IntegerField(unique=True)
    sigla = models.CharField(max_length=2)
    name  = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ['name']
        db_table = u'uf'


class Municipio(models.Model): 
    '''
        @Municipio: Modelo de dados com todas os Municipios.
    '''           
    federativa  = models.ForeignKey(UF,related_name='municipios')
    cod         = models.IntegerField(unique=True)
    name        = models.CharField(max_length=70)
    cep_inicial = models.IntegerField(unique=True)
    cep_final   = models.IntegerField(unique=True)
    ddd1        = models.IntegerField()
    ddd2        = models.IntegerField()
    
    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ['name']
        db_table = u'municipio'