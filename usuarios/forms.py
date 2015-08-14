#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import Select
from django.core.exceptions import ValidationError
from django.core.validators import EMPTY_VALUES
from django.utils.translation import ugettext, ugettext_lazy as _
from usuarios.models import Usuario
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

class UsuarioForm(forms.ModelForm):
    '''
      @UsuarioForm: Formulario para criação de um usuario
    '''
    password2 = forms.CharField(label=_("Confirmacao"),
        widget=forms.PasswordInput(attrs={'class':'form-control'}),help_text=_("Digite a mesma senha que a anterior, para verificacao."))

    class Meta:
        model = Usuario
        fields = ['first_name','last_name','grupo','email','username','password']

        widgets = { 'first_name'      : forms.TextInput(attrs={'class':'form-control','size':40}),
                    'last_name'       : forms.TextInput(attrs={'class':'form-control','size':40}),
                    'username'        : forms.TextInput(attrs={'class':'form-control','size':20}),            
                    'password'        : forms.PasswordInput(attrs={'class':'form-control','size':20}),
                    'email'           : forms.TextInput(attrs={'class': 'form-control','size':40}),    
                    'grupo'          : Select(attrs={'class': 'form-control'}),     
        }
    

    def clean_first_name(self):
        '''
            @clean_name: Transforma o nome em capitalizado
        '''
        nome            = self.cleaned_data['first_name']        
        return _x(nome)

    def clean_last_name(self):
        '''
            @clean_name: Transforma o nome em capitalizado
        '''
        sobrenome       = self.cleaned_data['last_name']
        return _x(sobrenome)       

    def clean_username(self):
        username = self.cleaned_data['username']
        
        if Usuario.objects.filter(
            username = username
            ).count():
            raise forms.ValidationError('Ja existe um usuário com este username')

        return username.lower()

    def clean_email(self):
        if Usuario.objects.filter(
            email=self.cleaned_data['email'],
            ).count():
            raise forms.ValidationError('Ja existe um usuário com este e-mail')

        return self.cleaned_data['email']   

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("As senha estão diferentes")

        return password2
    '''    
    def clean_grupo(self):
        grupo= self.cleaned_data['grupo']
                
        if grupo == '' or grupo == None:
            raise forms.ValidationError('Este campo é obrigatório.')
        
        return grupo
    '''
class UsuarioFormEditar(forms.ModelForm):
    '''
      @UsuarioFormEditar: Formulario para edicao de um usuario
    '''
    class Meta:
        model = Usuario
        fields = ['first_name','last_name','grupo','email','username']

        widgets = { 'first_name'      : forms.TextInput(attrs={'class':'form-control','size':40}),
                    'last_name'       : forms.TextInput(attrs={'class':'form-control','size':40}),
                    'username'        : forms.TextInput(attrs={'class':'form-control','readonly':'true','size':20}),
                    'email'           : forms.TextInput(attrs={'class': 'form-control','size':40}), 
                    'grupo'          : Select(attrs={'class': 'form-control'}),  
                                      
        }
    

    def clean_first_name(self):
        '''
            @clean_name: Transforma o nome em capitalizado
        '''
        nome            = self.cleaned_data['first_name']        
        return _x(nome)

    def clean_last_name(self):
        '''
            @clean_name: Transforma o nome em capitalizado
        '''
        sobrenome       = self.cleaned_data['last_name']
        return _x(sobrenome)       
   
    def clean_grupo(self):
        grupo= self.cleaned_data['grupo']
                
        if grupo == '' or grupo == None:
            raise forms.ValidationError('Este campo é obrigatório.')
        
        return grupo

class FormAlterarSenha(forms.Form):
    '''
      @FormAlterarSenha: Formulario para alteração da senha do usuario
    '''
    password1 = forms.CharField(label='Senha', max_length=32, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Senha'}))
    password2 = forms.CharField(label='Confirme a Senha', max_length=32, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirme'}))
    
    def clean(self):
        '''
        @clean: Verificar as senhas estão iguais
        '''
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise forms.ValidationError("Confirme seu senha")
        if password1 != password2:
            raise forms.ValidationError("As senha estão diferentes.")

        return self.cleaned_data 