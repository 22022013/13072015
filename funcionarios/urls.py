#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('funcionarios.views',
	
	url(r'^$','funcionarios', name='funcionarios'),	
	url(r'^novo/$', 'funcionario_novo', name='funcionario_novo'),
	url(r'^editar/(?P<id_funcionario>\d+)/$', 'funcionario_editar', name='funcionario_editar'),
	url(r'^alterar_status/(?P<id_funcionario>\d+)/$', 'funcionario_alterar_status', name='funcionario_alterar_status'),
	
)