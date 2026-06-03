from django.urls import path

from publisher.api.views import PublisherUpdateAndDelete, PublisherView

urlpatterns = [
    path('',PublisherView.as_view(), name = "publisher"),
    path('<int:pk>',PublisherUpdateAndDelete.as_view(), name = "publisher-update"),
]
