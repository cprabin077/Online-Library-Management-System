from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from notification.models import Notification
from notification.api.serializer import NotificationSerializer


class NotificationView(GenericAPIView):
    serializer_class = NotificationSerializer

    def get(self, request):
        notifications = Notification.objects.all()

        # unread filter
        unread = request.query_params.get("unread")

        if unread is not None:
            if unread.lower() == "true":
                notifications = notifications.filter(is_read=False)
            elif unread.lower() == "false":
                notifications = notifications.filter(is_read=True)

        serializer = self.get_serializer(notifications, many=True)
        return Response(serializer.data, status=200)


class NotificationReadView(GenericAPIView):
    serializer_class = NotificationSerializer

    def patch(self, request, pk):
        notification = Notification.objects.get(id=pk)

        serializer = self.get_serializer(
            notification, data={"is_read": True}, partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "Notification marked as read"}, status=200)


class NotificationUnreadCountView(GenericAPIView):

    def get(self, request):
        unread_count = Notification.objects.filter(is_read=False).count()

        return Response({"unread_count": unread_count}, status=200)
