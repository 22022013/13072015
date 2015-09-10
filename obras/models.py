#coding:utf-8
from django.db import models
from core.models import UF,Municipio

STATUS_OBRA = (
    ('aguardando','Aguardando'),
    ('em_andamento','Em Andamento'),
    ('finalizada','Finalizada'),
)

class Obra(models.Model):
    #cliente 			= models.ForeignKey(Cliente,blank=True,null=True,related_name="cliente")
    descricao           = models.CharField(max_length=500)
    estado              = models.ForeignKey(UF,blank=True,null=True)
    municipio           = models.ForeignKey(Municipio,blank=True,null=True)
    bairro              = models.CharField(max_length=50,blank=True,null=True)
    endereco            = models.CharField(max_length=30,blank=True,null=True,verbose_name='Endereço')
    numero              = models.CharField(max_length=10,blank=True,null=True)
    complemento			= models.CharField(max_length=30,blank=True,null=True)
    data_inicio         = models.DateField(blank=True,null=True)
    data_termino        = models.DateField(blank=True,null=True)
    status              = models.CharField(max_length=20,choices=STATUS_OBRA)
    ativo           	= models.BooleanField(default=True)
    
    def __unicode__(self):
        return '%s' % (self.id)

    class Meta:
        db_table = u'obra'

