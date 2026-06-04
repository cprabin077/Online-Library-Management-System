from django.urls import path
from borrow.api.views import BorrowView, ReturnBookView, OverdueBooksView

urlpatterns = [

    path('', BorrowView.as_view(), name='borrow'),

    path('<int:pk>/return/', ReturnBookView.as_view(), name='return'),

    path('overdue/', OverdueBooksView.as_view(), name='overdue'),
]