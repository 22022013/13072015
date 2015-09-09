#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('obras.views',
	
	url(r'^$','obras', name='obras'),	
	url(r'^nova/$', 'obra_nova', name='obra_nova'),
	url(r'^editar/(?P<id>\d+)/$', 'obra_editar', name='obra_editar'),
	url(r'^alterar_status/(?P<id>\d+)/$', 'obra_alterar_status', name='obra_alterar_status'),
		
)