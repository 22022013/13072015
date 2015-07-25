#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('servicos.views',
	
	#servico
	url(r'^$','servicos', name='servicos'),	
	url(r'^novo/$', 'servico_novo', name='servico_novo'),
	url(r'^novo/modal/$', 'servico_novo_modal', name='servico_novo_modal'),
	url(r'^editar/(?P<servico_id>\d+)/$', 'servico_editar', name='servico_editar'),
	url(r'^alterar_status/(?P<servico_id>\d+)/$', 'servico_alterar_status', name='servico_alterar_status'),
	#tipos servico
	url(r'^tipos/$','tipos_servico', name='tipos_servico'),	
	url(r'^novo/tipo$', 'tipo_servico_novo', name='tipo_servico_novo'),
	url(r'^novo/tipo/modal/$', 'tipo_servico_novo_modal', name='tipo_servico_novo_modal'),
	url(r'^get_tipos_servico/$', 'get_tipos_servico', name='get_tipos_servico'),
	url(r'^editar/tipo/(?P<tipo_servico_id>\d+)/$', 'tipo_servico_editar', name='tipo_servico_editar'),
	url(r'^alterar_status/tipo/(?P<tipo_servico_id>\d+)/$', 'tipo_servico_alterar_status', name='tipo_servico_alterar_status'),
)