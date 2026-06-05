from django.urls import path

from notification.api.views import NotificationReadView, NotificationUnreadCountView, NotificationView

urlpatterns = [
    path('', NotificationView.as_view(), name='notification'),
    path("<int:pk>/read/", NotificationReadView.as_view(), name="notification-read"),
    path("unread-count/", NotificationUnreadCountView.as_view(), name= "notification-unread-count"),

]