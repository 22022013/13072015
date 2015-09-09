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

        fields = ['descricao','estado','municipio','bairro','endereco','numero','complemento']

        widgets = { 'descricao'        : forms.Textarea(attrs={'class':'form-control','cols': 50, 'rows': 5}),
                    'estado'      : Select(attrs={'class':'form-control'}),
                    'municipio'   : Select(attrs={'class':'form-control'}),
                    'bairro'      : forms.TextInput(attrs={'class':'form-control','size':30}),
                    'endereco'    : forms.TextInput(attrs={'class':'form-control','size':50}),
                    'numero'      : forms.TextInput(attrs={'class':'form-control','size':10}),
                    'complemento' : forms.TextInput(attrs={'class':'form-control','size':20}),
                }
