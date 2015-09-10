#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import Select

from .models import Obra


class ObraForm(forms.ModelForm):
    '''
      @ObraForm: 
    '''
    class Meta:
        model = Obra

        fields = ['descricao','status','data_inicio','data_termino','estado','municipio','bairro','endereco','numero','complemento']

        widgets = { 'descricao'   : forms.Textarea(attrs={'class':'form-control','cols': 50, 'rows': 5}),
                    'estado'      : Select(attrs={'class':'form-control'}),
                    'status'      : Select(attrs={'class':'form-control'}),
                    'data_inicio' : forms.DateInput(attrs={'class': 'form-control','size':10}),
                    'data_termino': forms.DateInput(attrs={'class': 'form-control','size':10}),
                    'municipio'   : Select(attrs={'class':'form-control'}),
                    'bairro'      : forms.TextInput(attrs={'class':'form-control','size':30}),
                    'endereco'    : forms.TextInput(attrs={'class':'form-control','size':50}),
                    'numero'      : forms.TextInput(attrs={'class':'form-control','size':10}),
                    'complemento' : forms.TextInput(attrs={'class':'form-control','size':20}),
                }

    def clean(self):
        '''
        @clean: 
        '''
        status = self.cleaned_data.get('status')
        data_inicio  = self.cleaned_data.get('data_inicio')
        data_termino = self.cleaned_data.get('data_termino')
        msg = 'Este campo é obrigatório.'
        
        
        if status == "finalizada":
            if not data_inicio :
                self.add_error('data_inicio', msg)
            if not data_termino :
                self.add_error('data_termino', msg)    

        elif status == "em_andamento":
            if not data_inicio :
                self.add_error('data_inicio', msg)

        return self.cleaned_data 