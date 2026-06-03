from django.urls import path

from author.api.views import AuthorUpdate, AuthorView

urlpatterns = [
    path('',AuthorView.as_view(), name = "author"),
    path('<int:pk>',AuthorUpdate.as_view(), name = "author"),
]
