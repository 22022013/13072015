#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('vegetativo.views',
	
	#servico
	url(r'^os$','ordens_servico', name='ordens_servico'),	
	url(r'^os/nova/$', 'os_nova', name='os_nova'),
	url(r'^os/(?P<os_id>\d+)/editar/$', 'os_editar', name='os_editar'),
	#url(r'^alterar_status/(?P<servico_id>\d+)/$', 'servico_alterar_status', name='servico_alterar_status'),
	)