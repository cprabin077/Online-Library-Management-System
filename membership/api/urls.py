from django.urls import path

from membership.api.views import MembershipUpdateAndDelete, MembershipView


urlpatterns = [
    path('', MembershipView.as_view(), name='membership'),
    path('<int:pk>', MembershipUpdateAndDelete.as_view(), name='member-update'),
]