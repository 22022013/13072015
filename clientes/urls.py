#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('clientes.views',
	
	url(r'^$','clientes', name='clientes'),	
	url(r'^get_clientes/$','get_clientes',name='get_clientes'),
	url(r'^novo/$', 'cliente_novo', name='cliente_novo'),
	url(r'^novo/modal/$', 'cliente_novo_modal', name='cliente_novo_modal'),
	url(r'^editar/(?P<id>\d+)/$', 'cliente_editar', name='cliente_editar'),
	url(r'^alterar_status/(?P<id>\d+)/$', 'cliente_alterar_status', name='cliente_alterar_status'),
	
)