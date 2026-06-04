from django.urls import path

from librarian.api.views import LibrarianView, LibrarianUpdateAndDelete

urlpatterns = [
    path('', LibrarianView.as_view(), name="librarian"),
    path("<int:pk>", LibrarianUpdateAndDelete.as_view(), name="librarian-update"),
]
