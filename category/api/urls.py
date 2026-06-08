from django.urls import path

from category.api.views import CategoryUpdate, CategoryView

urlpatterns = [
    path('',CategoryView.as_view(), name = "category"),
    path('<int:pk>/',CategoryUpdate.as_view(), name = "category-update"),
]
