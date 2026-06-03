from django.urls import path
from .views import MemberView, MemberDetailView

urlpatterns = [
    path('', MemberView.as_view(), name='member-list-create'),
    path('<int:pk>', MemberDetailView.as_view(), name='member-detail'),
]