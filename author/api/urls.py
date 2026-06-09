from django.urls import path

from author.api.views import  AuthorUpdateAndDelete, AuthorView

urlpatterns = [
    path('',AuthorView.as_view(), name = "author"),
    path('<int:pk>',AuthorUpdateAndDelete.as_view(), name = "author-update"),
]
