from django.urls import path
from member.api.views import MemberApproveView, MemberView, MemberDetailView

urlpatterns = [
    path('', MemberView.as_view(), name='member-list-create'),
    path("approve/<int:pk>/", MemberApproveView.as_view()),
    path('<int:pk>', MemberDetailView.as_view(), name='member-detail'),
]