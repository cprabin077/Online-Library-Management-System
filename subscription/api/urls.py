from django.urls import path

from subscription.api.views import SubscriptionUpdate, SubscriptionView


urlpatterns = [
    path("", SubscriptionView.as_view(), name="subscription"),
    path("<int:pk>", SubscriptionUpdate.as_view(), name="subscription-update"),
]
