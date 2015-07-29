#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from servicos.models import Servico
from core.models import UF, Municipio

TIPO_ABRIGO = (
	('kit_cavalete','Kit Cavalete'),
	('abrigo_parede','Abrigo Parede'),
	('abrigo_fibra','Abrigo Fibra'),
	('abrigo_piso','Abrigo Piso'),
	)

class OrdemServico(models.Model):
	'''
		@OrdemServico: Modelo para uma nova ordem de servico
	''' 
	matricula 			= models.CharField(max_length=50,blank=True,null=True)
	os 		 			= models.CharField(max_length=50,blank=True,null=True)		
	tipo_servico 		= models.ForeignKey(Servico,blank=True,null=True,related_name="tipo_servico_vegetativo")
	equipe 				= models.CharField(max_length=100,blank=True,null=True)
	estado          	= models.ForeignKey(UF,blank=True,null=True)
	municipio       	= models.ForeignKey(Municipio,blank=True,null=True)
	bairro          	= models.CharField(max_length=30,blank=True,null=True)
	endereco        	= models.CharField(max_length=50,blank=True,null=True,verbose_name='Endereço')
	complemento        	= models.CharField(max_length=50,blank=True,null=True)
	numero          	= models.CharField(max_length=10,blank=True,null=True)
	hd_novo 			= models.CharField(max_length=15,blank=True,null=True)
	lacre_relojoaria	= models.CharField(max_length=15,blank=True,null=True)
	lacre_virola		= models.CharField(max_length=15,blank=True,null=True)
	data_solicitacao 	= models.DateField(blank=True,null=True)
	data_execucao	 	= models.DateField(blank=True,null=True)
	pead 				= models.DecimalField(default=0.00,max_digits=10,decimal_places=2)
	tipo_abrigo 		= models.CharField(max_length=15,blank=True,null=True,choices=TIPO_ABRIGO)
	calcada 			= models.DecimalField(default=0.00,max_digits=10,decimal_places=2)
	paralelo 			= models.DecimalField(default=0.00,max_digits=10,decimal_places=2)
	grama 				= models.DecimalField(default=0.00,max_digits=10,decimal_places=2)
	asfalto 			= models.DecimalField(default=0.00,max_digits=10,decimal_places=2)

	def __unicode__(self):
		return '%s' % (self.os)

