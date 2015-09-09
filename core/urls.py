#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('core.views',
  	url(r'^$', 'home', name='home'),
  	url(r'^notificacao_vista/$', 'notificacao_vista', name='notificacao_vista'),
  	url(r'^get_municipios/$', 'get_municipios', name='get_municipios'),

  	
)