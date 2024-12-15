from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import Notification

class NotificationListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        notifications = request.user.notifications.filter(unread=True)
        data = [{
            "id": notif.id,
            "actor": notif.actor.username,
            "verb": notif.verb,
            "timestamp": notif.timestamp,
            "target": str(notif.target)
        } for notif in notifications]
        
        # Mark notifications as read
        notifications.update(unread=False)
        
        return Response(data, status=200)

