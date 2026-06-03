from django.urls import path

from book.api.views import BookUpdateAndDelete, BookView

urlpatterns = [
    path('',BookView.as_view(), name = "book"),
    path('<int:pk>',BookUpdateAndDelete.as_view(), name = "book-update"),
]
