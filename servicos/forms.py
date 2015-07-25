#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import Select
from django.core.exceptions import ValidationError
from django.core.validators import EMPTY_VALUES
from django.utils.translation import ugettext, ugettext_lazy as _
from servicos.models import Servico,TipoServico
import re


class TipoServicoForm(forms.ModelForm):
	'''
	  @TipoServicoForm: Formulario para criação de um Subtipo de Serviço
	'''
	   
	class Meta:
		model = TipoServico
		fields = ['nome']

		widgets = { 'nome'        : forms.TextInput(attrs={'class':'form-control','size':30}),
		}

class ServicoForm(forms.ModelForm):
	'''
	  @ServicoForm: Formulario para criação de um Tipo de Serviço
	'''
	   
	class Meta:
		model = Servico
		fields = ['nome','tipo']

		widgets = { 
			'tipo'	  : Select(attrs={'class':'form-control'}),    
			'nome'    : forms.TextInput(attrs={'class':'form-control','size':30}),
					
		}