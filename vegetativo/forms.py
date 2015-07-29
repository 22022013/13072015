#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import Select
from vegetativo.models import OrdemServico

class OrdemServicoForm(forms.ModelForm):
	'''
	  @OrdemServicoForm: Formulario para cadastro das ordens de servico
	'''
	class Meta:
		model = OrdemServico

		fields = ['matricula','os','tipo_servico','equipe','estado','municipio','bairro','endereco','numero','complemento',
				'hd_novo','lacre_relojoaria','lacre_virola','data_solicitacao','data_execucao','pead','tipo_abrigo',
				'calcada','paralelo','grama','asfalto']
		widgets = { 
					'matricula' 		: forms.TextInput(attrs={'class':'form-control','size':10}),	
					'os' 		 		: forms.TextInput(attrs={'class':'form-control','size':10}),	
					'tipo_servico' 		: Select(attrs={'class':'form-control'}),
					'equipe' 			: forms.TextInput(attrs={'class':'form-control','size':15}),		
					'estado'          	: Select(attrs={'class':'form-control'}),
					'municipio'       	: Select(attrs={'class':'form-control'}),
					'bairro'          	: forms.TextInput(attrs={'class':'form-control','size':20}),	
					'endereco'        	: forms.TextInput(attrs={'class':'form-control','size':50}),	
					'numero'			: forms.TextInput(attrs={'class':'form-control','size':5}),	
					'complemento'       : forms.TextInput(attrs={'class':'form-control','size':20}),	   	
					'hd_novo' 			: forms.TextInput(attrs={'class':'form-control','size':10}),	
					'lacre_relojoaria'	: forms.TextInput(attrs={'class':'form-control','size':10}),	
					'lacre_virola'		: forms.TextInput(attrs={'class':'form-control','size':10}),	
					'data_solicitacao' 	: forms.DateInput(attrs={'class': 'form-control','size':10}),
					'data_execucao'	 	: forms.DateInput(attrs={'class': 'form-control','size':10}),
					'pead' 				: forms.TextInput(attrs={'class':'form-control','size':5,'localization': True}),	
					'tipo_abrigo' 		: Select(attrs={'class':'form-control'}),
					'calcada' 			: forms.TextInput(attrs={'class':'form-control','size':5,'localization': True}),	
					'paralelo' 			: forms.TextInput(attrs={'class':'form-control','size':5,'localization': True}),	
					'grama' 			: forms.TextInput(attrs={'class':'form-control','size':5,'localization': True}),	
					'asfalto'           : forms.TextInput(attrs={'class':'form-control','size':5,'localization': True}),	     
				}

	def __init__(self, *args, **kwargs):
		super(OrdemServicoForm, self).__init__(*args, **kwargs)
		self.fields['pead'].localize = True
		self.fields['pead'].widget.is_localized = True
		self.fields['calcada'].localize = True
		self.fields['calcada'].widget.is_localized = True
		self.fields['paralelo'].localize = True
		self.fields['paralelo'].widget.is_localized = True
		self.fields['grama'].localize = True
		self.fields['grama'].widget.is_localized = True
		self.fields['asfalto'].localize = True
		self.fields['asfalto'].widget.is_localized = True
