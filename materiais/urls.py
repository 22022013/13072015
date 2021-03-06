#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('materiais.views',
	
	url(r'^$','materiais', name='materiais'),	
	url(r'^novo/$', 'material_novo', name='material_novo'),
	url(r'^novo/modal/$', 'material_novo_modal', name='material_novo_modal'),
	url(r'^editar/(?P<id>\d+)/$', 'material_editar', name='material_editar'),
	url(r'^alterar_status/(?P<id>\d+)/$', 'material_alterar_status', name='material_alterar_status'),
	
	#equipamentos
	url(r'^equipamentos/$','equipamentos', name='equipamentos'),	
	url(r'^equipamento/novo/$', 'equipamento_novo', name='equipamento_novo'),
	url(r'^equipamento/editar/(?P<id>\d+)/$', 'equipamento_editar', name='equipamento_editar'),
	url(r'^equipamento/alterar_status/(?P<id>\d+)/$', 'equipamento_alterar_status', name='equipamento_alterar_status'),
)