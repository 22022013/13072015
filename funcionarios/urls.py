#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('funcionarios.views',
	
	url(r'^$','funcionarios', name='funcionarios'),	
	url(r'^novo/$', 'funcionario_novo', name='funcionario_novo'),
	url(r'^editar/(?P<id_funcionario>\d+)/$', 'funcionario_editar', name='funcionario_editar'),
	url(r'^alterar_status/(?P<id_funcionario>\d+)/$', 'funcionario_alterar_status', name='funcionario_alterar_status'),
	
	#Funcao
	url(r'^funcoes/$', 'funcoes', name='funcoes'),
	url(r'^funcao/nova/$', 'funcao_nova', name='funcao_nova'),
	url(r'^funcao/nova/modal/$', 'funcao_nova_modal', name='funcao_nova_modal'),
	url(r'^get_funcoes/$', 'get_funcoes', name='get_funcoes'),
	url(r'^funcao/editar/(?P<id_funcao>\d+)/$', 'funcao_editar', name='funcao_editar'),
	url(r'^funcao/alterar_status/(?P<id_funcao>\d+)/$', 'funcao_alterar_status', name='funcao_alterar_status'),
)