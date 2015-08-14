#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('usuarios.views',
	
	url(r'^$','usuarios', name='usuarios'),
	url(r'^novo/$', 'usuario_novo', name='usuario_novo'),
	url(r'^editar/(?P<usuario_id>\d+)/$', 'usuario_editar', name='usuario_editar'),
	url(r'^alterar_senha/$', 'alterar_senha', name='alterar_senha'),	
	url(r'^alterar_status/(?P<usuario_id>\d+)/$', 'usuario_alterar_status', name='usuario_alterar_status'),
	
	url(r'^esqueci_minha_senha/$', 'esqueci_senha', name='esqueci_senha'),  
	url(r'^recuperar_senha/(?P<usuario_hash>[a-fA-F0-9]{32})/$', 'recuperar_senha', name='recuperar_senha'),

	url(r'^email_recuperar_senha/(?P<id_cliente>\d+)/$', 'email_recuperar_senha', name='email_recuperar_senha'), 
	url(r'^email_reenviar_senha/(?P<id_cliente>\d+)/$', 'email_reenviar_senha', name='email_reenviar_senha'),
)