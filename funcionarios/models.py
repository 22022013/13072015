#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from usuarios.models import Usuario
from core.models import Notification

class Funcao(models.Model):
    '''
        @Funcao: Modelo para uma nova funcao
    ''' 
    nome      = models.CharField(max_length=100,unique=True)
    ativo     = models.BooleanField(default=True)
   
    def __unicode__(self):
        return '%s' % (self.nome)

    class Meta:
        db_table = u'funcao'

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

    class Meta:
        db_table = u'funcionario'

    def get_absolute_url(self):
        return "funcionarios/editar/%i/" % self.id

    def notify_novo_funcionario(self):
        
        usuarios = Usuario.objects.filter(is_active=True)
        for usuario in usuarios:
            n = Notification(notification_type=Notification.NOVO_FUNCIONARIO,
                funcionario=self,to_user=usuario).save()
'''
    def notify_remocao_funcionario(self,escola):
        escola = convert_escola(escola)
        diretores = escola.diretores.all()
        for d in diretores:
            n = Notification(notification_type=Notification.REMOCAO_FUNCIONARIO,
                funcionario=self.matricula.funcionario,
                to_user=d.user).save()

    def notify_edicao_funcionario(self,escola):
        escola = convert_escola(escola)
        diretores = escola.diretores.all()
        for d in diretores:
            n = Notification(notification_type=Notification.EDICAO_FUNCIONARIO,
                funcionario=self.matricula.funcionario,
                to_user=d.user).save()
'''