from django.urls import path

from publisher.api.views import PublisherUpdate, PublisherView

urlpatterns = [
    path('',PublisherView.as_view(), name = "publisher"),
    path('<int:pk>',PublisherUpdate.as_view(), name = "publisher-update"),
]
