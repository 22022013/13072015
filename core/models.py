#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.
from django.utils.html import escape

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

class Notification(models.Model):
    #FUNCIONARIO
    NOVO_FUNCIONARIO = 'NF'
    #EDICAO_FUNCIONARIO = 'EF'
    #DESATIVACAO_FUNCIONARIO = 'DF'
   

    NOTIFICATION_TYPES = (
        (NOVO_FUNCIONARIO, 'Novo Funcionário'),
        #(EDICAO_FUNCIONARIO, 'Edição de um Funcionário'),
        #(DESATIVACAO_FUNCIONARIO, 'Desativação de um Funcionário'),
        
    )

    _NOVO_FUNCIONARIO = u'Novo <b>funcionário</b> <a href="{0}">{1}</a>'
    #_EDICAO_FUNCIONARIO = u'O <b>funcionario</b> <a href="{0}">{1}</a> teve seus dados alterados.'
    #_REMOCAO_FUNCIONARIO = u'O <b>funcionario</b> {0} foi desativado.'

    
    to_user = models.ForeignKey(User, related_name='+')
    date = models.DateTimeField(auto_now_add=True)
    funcionario = models.ForeignKey('funcionarios.Funcionario', null=True, blank=True)
    notification_type = models.CharField(max_length=1, choices=NOTIFICATION_TYPES)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
        ordering = ('-date',)

    def __unicode__(self):
        if self.notification_type == self.NOVO_FUNCIONARIO:
            msg =  self._NOVO_FUNCIONARIO.format(
                self.funcionario.get_absolute_url(),
                self.funcionario.nome,
                )
            return msg
            '''    
            elif self.notification_type == self.EDICAO_FUNCIONARIO:
                msg =  self._EDICAO_FUNCIONARIO.format(
                    self.funcionario.novo(),
                    self.funcionario.nome,
                    )
                return msg
            elif self.notification_type == self.DESATIVACAO_FUNCIONARIO:
                msg =  self._DESATIVACAO_FUNCIONARIO.format(
                    self.funcionario.nome,
                    )
                return msg
            '''


            """
                    elif self.notification_type == self.EDICAO_FUNCIONARIO:
            return self._COMMENTED_TEMPLATE.format(
                escape(self.from_user.username),
                escape(self.from_user.profile.get_screen_name()),
                self.feed.pk,
                escape(self.get_summary(self.feed.post))
                #)
            """
        else:
            return 'Ooops! Algo inesperado aconteceu.'
