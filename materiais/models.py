#coding:utf-8
from django.db import models

UNIDADE = (
    ('1','UND'),
    ('2','M'),
)

class Material(models.Model):
    nome                  = models.CharField(max_length=100,unique=True)
    referencia            = models.TextField(blank=True,null=True)
    unidade				  = models.CharField(max_length=1,blank=True,null=True,choices=UNIDADE)
    estoque_atual         = models.IntegerField(default=0)
    ativo           	  = models.BooleanField(default=True)
    
    def __unicode__(self):
        return '%s' % (self.nome)

    class Meta:
        db_table = u'material'

class Equipamento(models.Model):
    nome          = models.CharField(max_length=100,unique=True)
    quantidade    = models.IntegerField(default=0)
    ativo         = models.BooleanField(default=True)
    
    def __unicode__(self):
        return '%s' % (self.nome)

    class Meta:
        db_table = u'equipamento'