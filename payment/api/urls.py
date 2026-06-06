from django.urls import path

from payment.api.views import ConfirmPaymentView


urlpatterns = [
    path("<int:pk>", ConfirmPaymentView.as_view(), name="payment"),

]
