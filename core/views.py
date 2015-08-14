#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import user_passes_test,login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse as r
from core.models import Notification


def group_required(*group_names):
	"""
		@group_required Requires user membership in at least one of the groups passed in.
	"""

	def in_groups(u):
		if u.is_authenticated():
			if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
				return True
		return False
	return user_passes_test(in_groups, login_url='/erro/401/')

def verifica_membro(user,grupo):
	'''
		@verifica_membro: Verificar se usuario faz parte de um determinado Grupo
	''' 
	return user.groups.filter(name=str(grupo)).exists()


def home(request):

	return render(request,"home.html")


@login_required
def notifications(request):
    user = request.user
    notifications = Notification.objects.filter(to_user=user)[:10]
    unread = Notification.objects.filter(to_user=user, is_read=False)
    for notification in unread:
        notification.is_read = True
        notification.save()        
    return render(request, 'core/notifications.html', {'notifications': notifications})
import time
@login_required
def notificacao_vista(request):
    user = request.user
    notifications = Notification.objects.filter(to_user=user, is_read=False)[:5]
    for notification in notifications:
        notification.is_read = True
        notification.save()
    return HttpResponse("ok")
    
    

@login_required
def check_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(to_user=user, is_read=False)[:5]
    return HttpResponse(len(notifications))
        