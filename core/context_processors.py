#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.models import Notification

def notification_processor(request):
	try :
		user = request.user
		notifications = Notification.objects.filter(to_user=user, is_read=False)[:5]
		num_notifications = notifications.count()
	except:
		notifications = ""
		num_notifications = 0

	return {'notifications': notifications,'num_notifications':num_notifications}

