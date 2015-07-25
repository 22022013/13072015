#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('materiais.views',
	
	url(r'^$','materiais', name='materiais'),	
	url(r'^novo/$', 'material_novo', name='material_novo'),
	url(r'^novo/modal/$', 'material_novo_modal', name='material_novo_modal'),
	url(r'^editar/(?P<material_id>\d+)/$', 'material_editar', name='material_editar'),
	url(r'^alterar_status/(?P<material_id>\d+)/$', 'material_alterar_status', name='material_alterar_status'),
	
)