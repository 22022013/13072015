#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.forms.widgets import Select
from django.core.exceptions import ValidationError
from django.core.validators import EMPTY_VALUES
from django.utils.translation import ugettext, ugettext_lazy as _
from funcionarios.models import Funcionario,Funcao
import re


def _x(nome): 
	""" 
	@_x: Função para remover caracteres especiais e espacamentos indevidos de uma string
	"""
	pro = ['\'','"','!','1','2','3','4','5','6','7','8','9','0','@','#','$','%','&','*','(',')','-','_','=','+','[',']','{','}','`','^','\'','?','.',',','\\','/','~']
	for p in pro:
		nome = nome.replace(p,' ')
	#return ' '.join(unicodedata.normalize('NFKD', nome.upper().strip()).encode('ascii', 'ignore').split())
	return nome.upper().strip()
  

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


class FuncionarioForm(forms.ModelForm):
	'''
	  @FuncionarioForm: Formulario para criação de um funcionario
	'''
	   
	class Meta:
		model = Funcionario
		fields = ['nome','funcao','cpf','telefone','celular']

		widgets = { 'nome'      : forms.TextInput(attrs={'class':'form-control','size':40}),
					'cpf'       : forms.TextInput(attrs={'class':'form-control','size':14}),  
					'celular'   : forms.TextInput(attrs={'class':'form-control','size':14}), 
					'telefone'  : forms.TextInput(attrs={'class':'form-control','size':14}),  
					'funcao'	: Select(attrs={'class':'form-control'}), 		 
		}	
	

	def clean_nome(self):
		'''
			@clean_nome: Transforma o nome em capitalizado
		'''
		nome            = self.cleaned_data['nome']

		if nome == '':
			 raise forms.ValidationError('Este campo é obrigatório.')
		
		return _x(nome)

	
	def clean_cpf(self):
		cpf= str(self.cleaned_data['cpf']).replace('.','').replace('-','').strip()
		
		if cpf != '':
			if validate_CPF(cpf): 
				return cpf
			else:
				raise forms.ValidationError('CPF invalido')
		else :
			cpf = None		

		return cpf


class FuncaoForm(forms.ModelForm):
	'''
	  @FuncaoForm: Formulario para criação de uma funcao
	'''
	   
	class Meta:
		model = Funcao
		fields = ['nome']

		widgets = { 'nome'        : forms.TextInput(attrs={'class':'form-control','size':40}),				 
		}
	

	def clean_nome(self):
		'''
			@clean_nome: Transforma o nome em capitalizado
		'''
		nome            = self.cleaned_data['nome']

		if nome == '':
			 raise forms.ValidationError('Este campo é obrigatório.')
		
		return nome.upper()