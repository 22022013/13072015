#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import Select
from django.core.exceptions import ValidationError
from django.core.validators import EMPTY_VALUES
from django.utils.translation import ugettext, ugettext_lazy as _
from materiais.models import Material,Equipamento
import re

class MaterialForm(forms.ModelForm):
	'''
	  @MaterialForm: Formulario para criação de um Material
	'''
	   
	class Meta:
		model = Material
		fields = ['nome','referencia','unidade','estoque_atual']

		widgets = { 'nome'       	 : forms.TextInput(attrs={'class':'form-control','size':30}),
					'referencia' 	 : forms.TextInput(attrs={'class':'form-control','size':30}),
					'unidade'	 	 : Select(attrs={'class':'form-control'}),    
					'estoque_atual'	 : forms.TextInput(attrs={'class':'form-control','size':5}),  
		}

class EquipamentoForm(forms.ModelForm):
	'''
	  @EquipamentoForm: Formulario para criação de um Equipamento
	'''
	   
	class Meta:
		model = Equipamento
		fields = ['nome','quantidade']

		widgets = { 'nome'        	: forms.TextInput(attrs={'class':'form-control','size':30}),
					'quantidade'	: forms.TextInput(attrs={'class':'form-control','size':5}),  
		}