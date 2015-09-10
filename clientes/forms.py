#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from django import forms
from django.forms.widgets import Select
from django.core.exceptions import ValidationError
from django.core.validators import EMPTY_VALUES
from django.utils.translation import ugettext, ugettext_lazy as _
from .models import Cliente



  

def verificar_igual(sequencia):
	"""
		@verificar_igual:
	"""    
	ultimo = '' 
	for seq in sequencia:        
		if ultimo == '':
			ultimo = seq
		
		if seq == ultimo:
			igual = True
		else:
			return False

		ultimo = seq
		
	return igual


def DV_maker(v):
	if v >= 2:
		return 11 - v
	return 0



def validate_CPF(value):
		"""
		Value can be either a string in the format XXX.XXX.XXX-XX or an
		11-digit number.
		"""
		if value in EMPTY_VALUES:
			return u''
		if not value.isdigit():
			value = re.sub("[-\.]", "", value)
		orig_value = value[:]
		try:
			int(value)
		except ValueError:
			return False
		if len(value) != 11 or value == "00000000000" or value == "11111111111" or value == "22222222222" or value == "33333333333" or \
			value == "44444444444" or value == "55555555555" or value == "66666666666" or value == "77777777777" or \
			value == "88888888888" or value == "99999999999":
			
			return False

		orig_dv = value[-2:]

		new_1dv = sum([i * int(value[idx]) for idx, i in enumerate(range(10, 1, -1))])
		new_1dv = DV_maker(new_1dv % 11)
		value = value[:-2] + str(new_1dv) + value[-1]
		new_2dv = sum([i * int(value[idx]) for idx, i in enumerate(range(11, 1, -1))])
		new_2dv = DV_maker(new_2dv % 11)
		value = value[:-1] + str(new_2dv)
		if value[-2:] != orig_dv:
			return False   


		return orig_value


class ClienteForm(forms.ModelForm):
	'''
	  @ClienteForm: Formulario para criação de um cliente
	'''
	   
	class Meta:
		model = Cliente
		fields = ['nome','tipo_cliente','cpf','cnpj','telefone','telefone2','email']

		widgets = { 'nome'        : forms.TextInput(attrs={'class':'form-control','size':40}),
					'tipo_cliente': Select(attrs={'class':'form-control'}),    
					'cpf'         : forms.TextInput(attrs={'class':'form-control','size':14}),  
					'cnpj'        : forms.TextInput(attrs={'class':'form-control','size':18}),
					'telefone'    : forms.TextInput(attrs={'class':'form-control','size':14}),  
					'telefone2'    : forms.TextInput(attrs={'class':'form-control','size':14}),  
					'email'       : forms.TextInput(attrs={'class':'form-control','size':30}),  
		}
		
	def clean_cpf(self):
		cpf= str(self.cleaned_data['cpf']).replace('.','').replace('-','').strip()
		tipo_cliente = self.cleaned_data.get('tipo_cliente')
		
		if tipo_cliente == 'fisica' :
			if cpf != '':
				if validate_CPF(cpf): 
					return cpf
				else:
					raise forms.ValidationError('CPF invalido')
			else :
				cpf = None
		else :
			cpf = None		

		return cpf

	def clean_cnpj(self):
		cnpj= str(self.cleaned_data['cnpj']).replace('.','').replace('-','').replace('/','').strip()
		if cnpj == '':
			cnpj = None
		return cnpj


