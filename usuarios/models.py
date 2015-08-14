#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User,Group

class Usuario(User):
    '''
        @Usuario: Modelo para um novo usuario
    ''' 
    hashcode            = models.CharField(max_length=40,blank=True,null=True) 
    password_textplan   = models.CharField(max_length=32,blank=True,null=True) 
    grupo               = models.ForeignKey(Group,blank=True,null=True)  

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

    